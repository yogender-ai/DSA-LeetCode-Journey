"""Regenerate README.md + assets/*.svg from the solutions in dates/ and LeetCode stats.

    python scripts/build.py

Derives streaks, RPG XP/levels, achievements, topic matrices, and date timelines.
"""
import datetime as dt
import json
import math
import os
import re
import sys
import urllib.request
from collections import Counter, OrderedDict, defaultdict
from xml.sax.saxutils import escape

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TZ = dt.timezone(dt.timedelta(hours=5, minutes=30))  # IST
REPO = "yogender-ai/DSA-LeetCode-Journey"
LEETCODE_USER = "yashyogender"

LANG = {".py": "Python", ".cpp": "C++", ".sql": "SQL"}

# Last successful API response, so a network blip degrades to slightly stale
# numbers instead of zeroing the dashboard. Committed alongside the README.
LC_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leetcode_stats.json")

LC_QUERY = """
query dashboardStats($u: String!) {
  matchedUser(username: $u) {
    username
    submitStatsGlobal { acSubmissionNum { difficulty count } }
    userCalendar { streak totalActiveDays submissionCalendar }
  }
  userContestRanking(username: $u) {
    rating
    globalRanking
    totalParticipants
    topPercentage
    attendedContestsCount
  }
}
"""


def _shape_leetcode(data):
    """Flatten LeetCode's GraphQL response into the fields the dashboard uses."""
    user = data["matchedUser"]
    counts = {b["difficulty"]: b["count"] for b in user["submitStatsGlobal"]["acSubmissionNum"]}
    cal = user.get("userCalendar") or {}
    rank = data.get("userContestRanking") or {}

    # submissionCalendar maps a UTC day timestamp to that day's submission count.
    heat = defaultdict(int)
    if cal.get("submissionCalendar"):
        for ts, n in json.loads(cal["submissionCalendar"]).items():
            day = dt.datetime.fromtimestamp(int(ts), dt.timezone.utc).date()
            heat[day.isoformat()] += int(n)

    return {
        "fetched_at": dt.datetime.now(TZ).isoformat(timespec="seconds"),
        "username": user.get("username") or LEETCODE_USER,
        "solved_total": counts.get("All", 0),
        "easy": counts.get("Easy", 0),
        "medium": counts.get("Medium", 0),
        "hard": counts.get("Hard", 0),
        "streak": cal.get("streak") or 0,
        "active_days": cal.get("totalActiveDays") or 0,
        "rating": round(rank.get("rating") or 0, 2),
        "global_ranking": rank.get("globalRanking") or 0,
        "total_participants": rank.get("totalParticipants") or 0,
        "top_pct": rank.get("topPercentage") or 0,
        "contests": rank.get("attendedContestsCount") or 0,
        "heat": dict(sorted(heat.items())),
    }


def fetch_leetcode_stats(user=LEETCODE_USER, timeout=25):
    """Live profile numbers straight from LeetCode's public GraphQL API.

    These used to be hardcoded constants, which meant the README froze at
    whatever was true the day someone typed them in.
    """
    req = urllib.request.Request(
        "https://leetcode.com/graphql/",
        data=json.dumps({"query": LC_QUERY, "variables": {"u": user}}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Referer": f"https://leetcode.com/u/{user}/",
            "User-Agent": "Mozilla/5.0 (compatible; DSA-Journey-Build/1.0)",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            payload = json.load(resp)
        data = (payload or {}).get("data") or {}
        if not data.get("matchedUser"):
            raise ValueError(f"LeetCode returned no profile for '{user}'")
        stats = _shape_leetcode(data)
        with open(LC_CACHE, "w", encoding="utf-8") as fh:
            json.dump(stats, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"[build] live LeetCode stats for {user}: {stats['solved_total']} solved "
              f"({stats['easy']}E / {stats['medium']}M / {stats['hard']}H), "
              f"streak {stats['streak']}, {stats['active_days']} active days")
        return stats
    except Exception as exc:
        print(f"[build] WARNING: live LeetCode fetch failed: {exc}")
        if os.path.exists(LC_CACHE):
            with open(LC_CACHE, encoding="utf-8") as fh:
                cached = json.load(fh)
            print(f"[build] falling back to cached stats from {cached.get('fetched_at')}")
            return cached
        raise SystemExit("[build] no live stats and no cache - refusing to build a wrong README")


DIFF_ICON = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

# Theme colors
BG, PANEL, EDGE = "#05060f", "#0b0d1a", "#1e1b4b"
VIOLET, CYAN, PINK, LIME, AMBER, TEAL = "#8b5cf6", "#22d3ee", "#f472b6", "#a3e635", "#fbbf24", "#2dd4bf"
TEXT, MUTED, DIM = "#e2e8f0", "#94a3b8", "#475569"
LEVELS = ["#161b33", "#3b1f7a", "#6d28d9", "#8b5cf6", "#c4b5fd"]
SANS = "'Segoe UI', 'SF Pro Display', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', 'SF Mono', Consolas, Menlo, monospace"

TOPICS_DEF = OrderedDict([
    ("Arrays & Hashing", ("🧮", "Counting, grouping, frequency maps, set lookups")),
    ("Two Pointers", ("👉", "Sorted arrays, inward shrink, opposite ends, palindromes")),
    ("Sliding Window", ("🪟", "Contiguous subarrays, window bounds, max/min in range")),
    ("Prefix Sum", ("➕", "Range queries, cumulative sums, equilibrium splits")),
    ("Stack", ("📚", "LIFO, monotonic stack, matching brackets, nearest greater")),
    ("Binary Search", ("🔍", "Sorted search space, monotonic condition, answer range")),
    ("Trees & BST", ("🌲", "Binary trees, BST traversal, BFS/DFS, recursion")),
    ("Graphs & Search", ("🕸️", "Adjacency list, BFS/DFS, cycle detection, topological sort")),
    ("Dynamic Programming", ("🧠", "Optimal substructure, memoization, bottom-up tabulation")),
    ("Matrix / Simulation", ("🔄", "2D grid traversals, spiral order, in-place rotations")),
    ("Strings", ("🔤", "Pattern matching, run-length compression, substrings")),
    ("Sorting & STL", ("🧰", "Custom comparators, sorting algorithms, priority queues")),
    ("SQL", ("🗄️", "Joins, aggregations, window functions, conditional CASE")),
    ("Bit Manipulation", ("⚡", "XOR tricks, bitmasks, bit count, power of two")),
    ("Data Structures & Algorithms", ("🧩", "Core concepts, foundations, algorithms"))
])


# ─────────────────────────────── parsing ───────────────────────────────
def parse_solution(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    with open(path, encoding="utf-8", errors="ignore") as f:
        head = [re.sub(r'^\s*(/\*+|\*/|\*|--|#|""")?\s?', "", l).rstrip() for l in f.read().splitlines()[:20]]
    text = "\n".join(head)
    
    ext = os.path.splitext(path)[1]
    e = {
        "path": rel,
        "lang": LANG.get(ext, "Code"),
        "num": None,
        "title": None,
        "diff": "Medium",
        "pattern": "Data Structures & Algorithms",
        "time": "O(n)",
        "space": "O(1)",
        "dates": [],
        "kind": "snippet",
        "url": None
    }
    
    m = re.search(r"LeetCode (\d+) · (.+?) · (Easy|Medium|Hard)", text)
    if m:
        e.update(kind="leetcode", num=int(m[1]), title=m[2], diff=m[3])
        u = re.search(r"https://leetcode\.com/problems/[\w-]+/", text)
        e["url"] = u[0] if u else f"https://leetcode.com/problemset/all/"
    elif re.search(r"DSA Lesson · (.+)", text):
        m2 = re.search(r"DSA Lesson · (.+)", text)
        e.update(kind="lesson", title=m2[1])
    else:
        # Check filename for problem number
        fn = os.path.basename(path)
        m_fn = re.match(r"^(\d{3,4})-(.+)", fn)
        if m_fn:
            e.update(kind="leetcode", num=int(m_fn[1]), title=m_fn[2].rsplit(".", 1)[0].replace("-", " ").title())
            e["url"] = f"https://leetcode.com/problems/{m_fn[2].rsplit('.', 1)[0]}/"
        else:
            e["title"] = fn.rsplit(".", 1)[0].replace("_", " ").replace("-", " ").title()

    for key, rx in (("pattern", r"Pattern\s*:\s*(.+)"), ("time", r"Time\s*:\s*(.+)"), ("space", r"Space\s*:\s*(.+)")):
        m = re.search(rx, text)
        if m and m[1].strip():
            e[key] = m[1].strip()
            
    m_dates = re.search(r"(?:Solved|Written|Date)\s*:\s*(.+)", text)
    if m_dates:
        for part in m_dates[1].split(","):
            part = part.strip()
            for fmt in ("%d %b %Y", "%Y-%m-%d", "%d-%m-%y"):
                try:
                    e["dates"].append(dt.datetime.strptime(part, fmt).date())
                    break
                except ValueError:
                    pass

    # If no date in header, parse from directory name like 01-02-26
    if not e["dates"]:
        m_dir = re.search(r"(\d{2})-(\d{2})-(\d{2})", rel)
        if m_dir:
            d, m, y = m_dir.groups()
            try:
                e["dates"].append(dt.date(2000 + int(y), int(m), int(d)))
            except:
                pass
                
    return e


def collect_solutions():
    out = []
    # Scan all yearly folders at root (e.g. 2025, 2026)
    for entry in sorted(os.listdir(ROOT)):
        if re.match(r"^20\d\d$", entry) and os.path.isdir(os.path.join(ROOT, entry)):
            year_dir = os.path.join(ROOT, entry)
            for root, _, files in os.walk(year_dir):
                for fn in sorted(files):
                    ext = os.path.splitext(fn)[1].lower()
                    if ext in LANG:
                        e = parse_solution(os.path.join(root, fn))
                        out.append(e)
    return out



# ─────────────────────────────── stats & RPG ───────────────────────────
def calculate_stats(entries):
    days = Counter(d for e in entries for d in e["dates"])
    ds = sorted(days)
    today = dt.datetime.now(TZ).date()
    
    # Official LeetCode stats, fetched live at build time.
    lc = fetch_leetcode_stats()
    lc_solved_total = lc["solved_total"]
    lc_easy = lc["easy"]
    lc_medium = lc["medium"]
    lc_hard = lc["hard"]
    lc_streak = lc["streak"]
    lc_active_days = lc["active_days"]
    lc_rating = lc["rating"]
    lc_top_pct = lc["top_pct"]

    # Heatmap from LeetCode's own submission calendar, so it reflects every
    # day you were active rather than only days a file landed in this repo.
    heat = {dt.date.fromisoformat(k): v for k, v in (lc.get("heat") or {}).items()}
    if not heat:
        heat = dict(days)

    longest, best_end, run = 0, None, 0
    for i, d in enumerate(ds):
        run = run + 1 if i and (d - ds[i - 1]).days == 1 else 1
        if run > longest:
            longest, best_end = run, d
    longest = max(longest, lc_streak)
    current_streak = lc_streak

    uniq_repo = {}
    for e in entries:
        if e["kind"] == "leetcode" and e["num"]:
            uniq_repo[e["num"]] = e["diff"]

    # RPG Formula
    # Easy: 10 XP, Medium: 25 XP, Hard: 50 XP, Active Day: 5 XP, Streak: 10 XP/day
    xp = (lc_easy * 10) + (lc_medium * 25) + (lc_hard * 50) + (lc_active_days * 5) + (current_streak * 10)
    level = math.floor(math.sqrt(xp / 25)) + 1
    xp_curr_level_base = ((level - 1) ** 2) * 25
    xp_next_level_target = (level ** 2) * 25
    level_progress = (xp - xp_curr_level_base) / max(1, xp_next_level_target - xp_curr_level_base)

    ranks = [
        (1, 4, "Code Apprentice ⚔️"),
        (5, 8, "Algorithm Initiate 🛡️"),
        (9, 12, "Data Structure Knight 🗡️"),
        (13, 16, "Pattern Master 🔮"),
        (17, 20, "Grandmaster Alchemist 👑"),
        (21, 99, "Algorithmic Mythic 🌌")
    ]
    rank_title = "Grandmaster Alchemist 👑"
    for lo, hi, title in ranks:
        if lo <= level <= hi:
            rank_title = title
            break

    last_entry = max(((d, e) for e in entries for d in e["dates"]), key=lambda x: (x[0], x[1]["kind"] == "leetcode")) if entries else (today, {})

    return dict(
        days=days, heat=heat, first=ds[0] if ds else today, last_day=ds[-1] if ds else today, today=today,
        current=current_streak, longest=longest,
        active=lc_active_days,
        solved_total=lc_solved_total, easy=lc_easy, medium=lc_medium, hard=lc_hard,
        repo_solved=len(uniq_repo), repo_entries=len(entries),
        rating=lc_rating, top_pct=lc_top_pct,
        contests=lc.get("contests", 0), global_ranking=lc.get("global_ranking", 0),
        total_participants=lc.get("total_participants", 0),
        fetched_at=lc.get("fetched_at", ""),
        xp=xp, level=level, rank_title=rank_title,
        level_progress=round(level_progress * 100, 1),
        xp_next_target=xp_next_level_target,
        last=last_entry,
        langs=sorted({e["lang"] for e in entries})
    )


# ─────────────────────────────── SVGs ──────────────────────────────────
def svg(w, h, inner, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="{escape(title)}"><title>{escape(title)}</title>{inner}</svg>\n')


def banner_svg(s):
    import random
    rnd = random.Random(42)
    W, H = 1200, 320
    tokens = ["O(n)", "{ }", "[i, j]", "dp[i][j]", "while l < r", "freq[x]++", "O(log n)", "stack.pop()", "∑", "→",
              "LEFT JOIN", "GROUP BY", "lps[i]", "prefix[i]", "O(1)", "set()", "window", "sort()", "3Sum", "BST",
              "BFS", "DFS", "two_pointers", "monotonic_stack", "memo", "bitmask"]
    floats = "".join(
        f'<text x="{rnd.randint(30, W - 90)}" y="{H + 20}" class="tk" style="animation-duration:{rnd.uniform(9, 16):.1f}s;'
        f'animation-delay:-{rnd.uniform(0, 16):.1f}s;font-size:{rnd.choice([12, 14, 16, 18])}px" fill="{rnd.choice([VIOLET, CYAN, PINK, MUTED])}">'
        f'{escape(t)}</text>' for t in tokens * 2)
    lines = [
        f"LEVEL {s['level']} {s['rank_title']} · {s['xp']:,} EXP",
        f"🔥 {s['current']}-DAY CONTINUOUS STREAK · {s['solved_total']} PROBLEMS SOLVED",
        f"CONTEST RATING {s['rating']} (TOP {s['top_pct']}%) · {s['active']} PRACTICE DAYS",
        "ORGANISED BY DATE & STREAK — POWERED BY CONSISTENCY"
    ]
    roll = "".join(f'<text x="600" y="235" class="rl" style="animation-delay:{i * 3.2:.1f}s">{escape(t)}</text>' for i, t in enumerate(lines))
    inner = f"""
<defs>
  <linearGradient id="g" x1="0" x2="1" spreadMethod="reflect"><stop offset="0" stop-color="{VIOLET}"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{PINK}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1 0;0 0" dur="8s" repeatCount="indefinite"/></linearGradient>
  <filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="50"/></filter>
  <clipPath id="c"><rect width="{W}" height="{H}" rx="24"/></clipPath>
</defs>
<style>
  .tk{{font-family:{MONO};opacity:0;animation:up linear infinite}}
  @keyframes up{{0%{{transform:translateY(0);opacity:0}}15%{{opacity:.18}}85%{{opacity:.18}}100%{{transform:translateY(-{H + 60}px);opacity:0}}}}
  .t{{font:800 58px {SANS};text-anchor:middle;letter-spacing:2px}} .k{{font:700 13px {MONO};letter-spacing:6px;fill:{MUTED};text-anchor:middle}}
  .rl{{font:600 18px {MONO};fill:{CYAN};text-anchor:middle;opacity:0;animation:rl 12.8s infinite}}
  @keyframes rl{{0%{{opacity:0;transform:translateY(12px)}}3%,22%{{opacity:1;transform:none}}25%,100%{{opacity:0;transform:translateY(-12px)}}}}
  .o1{{animation:o1 12s ease-in-out infinite}} .o2{{animation:o2 15s ease-in-out infinite}}
  @keyframes o1{{50%{{transform:translate(220px,40px)}}}} @keyframes o2{{50%{{transform:translate(-240px,-30px)}}}}
</style>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g filter="url(#b)" opacity=".7"><circle class="o1" cx="250" cy="110" r="150" fill="{VIOLET}"/><circle class="o2" cx="950" cy="190" r="150" fill="{CYAN}" opacity=".7"/></g>
  {floats}
  <text x="600" y="85" class="k">// DATA STRUCTURES &amp; ALGORITHMS · CHRONICLES</text>
  <rect x="120" y="105" width="960" height="150" rx="24" fill="{BG}" opacity=".6" filter="url(#b)"/>
  <text x="600" y="172" class="t" fill="url(#g)">DSA · LeetCode Journey</text>
  {roll}
</g>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="24" fill="none" stroke="{EDGE}"/>
"""
    return svg(W, H, inner, "DSA · LeetCode Journey")


def streak_svg(s):
    W, H = 1200, 420
    start = dt.date(2026, 1, 1) - dt.timedelta(days=(dt.date(2026, 1, 1).isoweekday() % 7))
    end = s["today"]
    weeks = (end - start).days // 7 + 1
    cell = min(15.0, (W - 80) / max(weeks, 1) - 4)
    step = cell + 4
    x0 = (W - weeks * step) / 2 + 2
    heat = s.get("heat") or s["days"]
    y0, mx = 205, max(heat.values()) if heat else 1
    cells, months = [], []
    d = start
    while d <= end:
        wi, wd = (d - start).days // 7, d.isoweekday() % 7
        c = heat.get(d, 0)
        lvl = 0 if c == 0 else min(4, 1 + round(3 * (c - 1) / max(mx - 1, 1)))
        tip = f"{d:%d %b %Y}: {c} submission{'s' if c != 1 else ''}" if c else f"{d:%d %b %Y}"
        extra = ' class="on" style="animation-delay:%.2fs"' % (wi * .04) if c else ""
        cells.append(f'<rect x="{x0 + wi * step:.1f}" y="{y0 + wd * step:.1f}" width="{cell:.1f}" height="{cell:.1f}" rx="3" fill="{LEVELS[lvl]}"'
                     f'{extra}><title>{tip}</title></rect>')
        if d.day == 1 or d == start:
            months.append(f'<text x="{x0 + wi * step:.1f}" y="{y0 - 10}" class="m">{d:%b}{" ’" + d.strftime("%y") if d.month == 1 or d == start else ""}</text>')
        d += dt.timedelta(days=1)
        
    tiles = [
        ("🔥 CURRENT STREAK", f"{s['current']} DAYS", "blazing flame · active today", LIME),
        ("🏆 LONGEST STREAK", f"{s['longest']} DAYS", "unbroken daily momentum", AMBER),
        ("📅 PRACTICE DAYS", f"{s['active']} DAYS", "lifetime active coding days", CYAN),
        ("⚔️ TOTAL SOLVED", f"{s['solved_total']}", f"{s['easy']} easy · {s['medium']} med · {s['hard']} hard", VIOLET)
    ]
    t = "".join(f'<g transform="translate({32 + i * 288} 26)"><rect width="272" height="114" rx="14" fill="{c}" fill-opacity=".08" stroke="{c}" stroke-opacity=".4"/>'
                f'<text x="18" y="30" class="lb" fill="{c}">{l}</text><text x="18" y="76" class="big">{v}</text><text x="18" y="98" class="sub">{escape(sb)}</text></g>'
                for i, (l, v, sb, c) in enumerate(tiles))
    legend = "".join(f'<rect x="{W - 170 + i * 19}" y="{H - 28}" width="14" height="14" rx="3" fill="{c}"/>' for i, c in enumerate(LEVELS))
    inner = f"""
<style>
  .lb{{font:700 12px {MONO};letter-spacing:1.5px}} .big{{font:800 36px {SANS};fill:{TEXT}}} .sub{{font:500 13px {SANS};fill:{MUTED}}}
  .m{{font:600 11px {MONO};fill:{MUTED}}} .u{{font:500 11px {MONO};fill:{DIM}}}
  .on{{animation:pop 5s ease-in-out infinite}} @keyframes pop{{0%,80%,100%{{opacity:1}}88%{{opacity:.35}}}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{PANEL}" stroke="{EDGE}"/>
{t}
{''.join(months)}
{''.join(cells)}
<text x="32" y="{H - 18}" class="u">2026 practice calendar · updated {s['today']:%d %b %Y} (IST)</text>
<text x="{W - 205}" y="{H - 18}" class="u">less</text>{legend}<text x="{W - 72}" y="{H - 18}" class="u">more</text>
"""
    return svg(W, H, inner, f"Streak: {s['current']} days current, {s['longest']} days longest, {s['active']} practice days")


def rpg_card_svg(s):
    W, H = 1200, 260
    bar_w = 700
    fill_w = max(10, bar_w * (s['level_progress'] / 100))
    # Quest targets move with you instead of sitting at a fixed 300.
    solved_goal = max(100, math.ceil((s['solved_total'] + 1) / 100) * 100)
    solved_pct = min(100, round(s['solved_total'] / solved_goal * 100))
    streak_pct = min(100, round(s['current'] / 100 * 100))
    inner = f"""
<defs>
  <linearGradient id="xp_grad" x1="0" x2="1"><stop offset="0%" stop-color="{VIOLET}"/><stop offset="100%" stop-color="{CYAN}"/></linearGradient>
</defs>
<style>
  .card_title{{font:800 24px {SANS};fill:{TEXT}}}
  .tag{{font:700 11px {MONO};letter-spacing:2px;fill:{AMBER}}}
  .stat_lbl{{font:600 13px {MONO};fill:{MUTED}}}
  .stat_val{{font:800 28px {SANS};fill:{TEXT}}}
  .badge{{font:700 12px {MONO};fill:{TEXT}}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{PANEL}" stroke="{EDGE}"/>
<g transform="translate(40, 36)">
  <text x="0" y="0" class="tag">// PLAYER PROFILE &amp; RPG LEVEL</text>
  <text x="0" y="34" class="card_title">Level {s['level']} — {s['rank_title']}</text>
  <text x="0" y="62" class="stat_lbl">Total EXP: <tspan fill="{CYAN}">{s['xp']:,} XP</tspan> · Progress to Level {s['level'] + 1}: <tspan fill="{LIME}">{s['level_progress']}%</tspan></text>
  
  <!-- XP Bar -->
  <rect x="0" y="80" width="{bar_w}" height="16" rx="8" fill="{EDGE}"/>
  <rect x="0" y="80" width="{fill_w}" height="16" rx="8" fill="url(#xp_grad)"/>
  <text x="{bar_w + 20}" y="93" class="stat_lbl">{s['xp']:,} / {s['xp_next_target']:,} XP</text>

  <!-- Small Stats Grid -->
  <g transform="translate(0, 120)">
    <text x="0" y="16" class="stat_lbl">CONTEST RATING</text>
    <text x="0" y="44" class="stat_val">{s['rating']}</text>
    <text x="0" y="62" class="stat_lbl" fill="{TEAL}">Top {s['top_pct']}% · 14 Contests</text>

    <text x="240" y="16" class="stat_lbl">TOTAL PROBLEMS</text>
    <text x="240" y="44" class="stat_val">{s['solved_total']}</text>
    <text x="240" y="62" class="stat_lbl">{s['repo_entries']} files tracked</text>

    <text x="480" y="16" class="stat_lbl">PRACTICE STREAK</text>
    <text x="480" y="44" class="stat_val" fill="{LIME}">🔥 {s['current']} Days</text>
    <text x="480" y="62" class="stat_lbl">Consistency Rank: S-Tier</text>
  </g>
</g>

<!-- Achievement Shield Box -->
<g transform="translate(860, 32)">
  <rect width="300" height="196" rx="14" fill="{BG}" stroke="{EDGE}"/>
  <text x="20" y="32" class="tag" fill="{PINK}">// ACTIVE QUESTS</text>
  <text x="20" y="65" class="badge">⚔️ Quest: Path to {solved_goal} Solved</text>
  <text x="20" y="85" class="stat_lbl" font-size="12">{s['solved_total']}/{solved_goal} problems ({solved_pct}% complete)</text>
  <rect x="20" y="95" width="260" height="6" rx="3" fill="{EDGE}"/>
  <rect x="20" y="95" width="{260 * solved_pct / 100:.0f}" height="6" rx="3" fill="{PINK}"/>

  <text x="20" y="130" class="badge">🔥 Quest: Century Flame (100d)</text>
  <text x="20" y="150" class="stat_lbl" font-size="12">{s['current']}/100 streak days ({streak_pct}% complete)</text>
  <rect x="20" y="160" width="260" height="6" rx="3" fill="{EDGE}"/>
  <rect x="20" y="160" width="{260 * streak_pct / 100:.0f}" height="6" rx="3" fill="{LIME}"/>
</g>
"""
    return svg(W, H, inner, f"Player Profile: Level {s['level']} {s['rank_title']}")


def topics_svg(entries):
    W = 1200
    rows = []
    # Count per pattern
    topic_counts = defaultdict(lambda: Counter())
    for e in entries:
        pat = e.get("pattern") or "Data Structures & Algorithms"
        # Map to canonical topic
        matched = next((k for k in TOPICS_DEF if k.lower() in pat.lower()), "Data Structures & Algorithms")
        topic_counts[matched][e.get("diff", "Medium") if e["kind"] == "leetcode" else "Other"] += 1

    for name, (emoji, _) in TOPICS_DEF.items():
        c = topic_counts[name]
        if sum(c.values()) > 0:
            rows.append((f"{emoji} {name}", c))

    mx = max(sum(c.values()) for _, c in rows) if rows else 1
    H = 70 + len(rows) * 34 + 36
    cols = [("Easy", TEAL), ("Medium", AMBER), ("Hard", PINK), ("Other", VIOLET)]
    out = []
    for i, (label, c) in enumerate(rows):
        y, x = 64 + i * 34, 330
        out.append(f'<text x="40" y="{y + 14}" class="l">{escape(label)}</text><rect x="330" y="{y}" width="760" height="18" rx="9" fill="{EDGE}" fill-opacity=".6"/>')
        for k, col in cols:
            if c[k]:
                w = 760 * c[k] / mx
                out.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w - 2, 4):.1f}" height="18" rx="9" fill="{col}" class="gr" style="animation-duration:{.8 + i * .08:.2f}s"/>')
                x += w
        out.append(f'<text x="{x + 10:.0f}" y="{y + 14}" class="n">{sum(c.values())}</text>')
    lg = "".join(f'<circle cx="{40 + i * 160}" cy="{H - 22}" r="6" fill="{col}"/><text x="{52 + i * 160}" y="{H - 17}" class="s">'
                 f'{"lessons / snippets" if k == "Other" else k}</text>' for i, (k, col) in enumerate(cols))
    inner = f"""
<style>
  .l{{font:600 15px {SANS};fill:{TEXT}}} .n{{font:700 13px {MONO};fill:{MUTED}}} .s{{font:500 13px {SANS};fill:{MUTED}}}
  .h{{font:700 13px {MONO};letter-spacing:3px;fill:{VIOLET}}}
  .gr{{transform-box:fill-box;transform-origin:left;animation:gr 1s cubic-bezier(.2,.8,.2,1)}} @keyframes gr{{from{{transform:scaleX(0)}}}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{PANEL}" stroke="{EDGE}"/>
<text x="40" y="38" class="h">// SOLUTIONS PER PATTERN &amp; TOPIC</text>
{''.join(out)}{lg}
"""
    return svg(W, H, inner, "Solutions per pattern & topic")


# ─────────────────────────────── markdown sections ──────────────────────
def link_name(e):
    if e["kind"] == "leetcode" and e.get("url"):
        return f"[{e['title']}]({e['url']})"
    return f"[{e['title']}]({e['path']})"


def fmt_dates(ds):
    return ", ".join(f"{d:%d %b %Y}" for d in sorted(ds))


def build_date_timeline(entries, s):
    by_day = defaultdict(list)
    seen_day_probs = defaultdict(set)
    for e in entries:
        ds = sorted(e["dates"])
        for i, d in enumerate(ds):
            key = (e["kind"], e["num"], e["title"])
            if key not in seen_day_probs[d]:
                seen_day_probs[d].add(key)
                by_day[d].append((e, i > 0))


    months = OrderedDict()
    for d in sorted(by_day, reverse=True):
        months.setdefault((d.year, d.month), []).append(d)

    # Overview tree
    tree = ["```text", "📅 dates/"]
    years = OrderedDict()
    for (y, m), ds in months.items():
        years.setdefault(y, []).append((m, ds))
    mx = max(sum(len(by_day[d]) for d in ds) for ds in months.values()) if months else 1
    for yi, (y, ms) in enumerate(years.items()):
        last_y = yi == len(years) - 1
        n_y = sum(len(by_day[d]) for _, ds in ms for d in ds)
        tree.append(f"{'└──' if last_y else '├──'} {y}/  ·  {n_y} solutions · {sum(len(ds) for _, ds in ms)} practice days")
        for mi, (m, ds) in enumerate(ms):
            n = sum(len(by_day[d]) for d in ds)
            bar = "█" * max(1, round(20 * n / mx))
            pre = "    " if last_y else "│   "
            tree.append(f"{pre}{'└──' if mi == len(ms) - 1 else '├──'} {dt.date(y, m, 1):%b}  {bar:<20}  {n:>2} solution{'s' if n != 1 else ' '} · {len(ds)} day{'s' if len(ds) > 1 else ''}")
    tree.append("```")

    out = ["\n".join(tree), ""]
    for i, ((y, m), ds) in enumerate(months.items()):
        n = sum(len(by_day[d]) for d in ds)
        out.append(f"<details{' open' if i == 0 else ''}>\n<summary><b>{dt.date(y, m, 1):%B %Y}</b> — {n} solution{'s' if n != 1 else ''} across {len(ds)} day{'s' if len(ds) > 1 else ''}</summary>\n")
        out.append("| Date | Problem / Lesson | Topic / Pattern | Diff | Code |\n|:--|:--|:--|:-:|:-:|")
        for d in ds:
            items = sorted(by_day[d], key=lambda x: (x[0]["kind"] != "leetcode", x[0]["num"] or 0, x[0]["title"]))
            for j, (e, revisit) in enumerate(items):
                day_str = f"**{d:%d %b}** ({d:%a})" if j == 0 else ""
                title_str = (f"{e['num']}. " if e["kind"] == "leetcode" else "") + link_name(e) + (" ↺ *revisit*" if revisit else "")
                diff_icon = DIFF_ICON.get(e["diff"], "📘")
                code_link = f"[{e['lang']}]({e['path']})"
                out.append(f"| {day_str} | {title_str} | {e['pattern']} | {diff_icon} {e['diff']} | {code_link} |")
        out.append("\n</details>\n")
    return "\n".join(out)


def build_topic_matrix(entries):
    topic_groups = defaultdict(list)
    for e in entries:
        pat = e.get("pattern") or "Data Structures & Algorithms"
        matched = next((k for k in TOPICS_DEF if k.lower() in pat.lower()), "Data Structures & Algorithms")
        topic_groups[matched].append(e)

    out = []
    for name, (emoji, signal) in TOPICS_DEF.items():
        es = topic_groups.get(name, [])
        if not es:
            continue
        lc = OrderedDict()
        for e in sorted((e for e in es if e["kind"] == "leetcode" and e["num"]), key=lambda e: e["num"]):
            r = lc.setdefault(e["num"], dict(e, files=[], dates=set()))
            r["files"].append(f"[{e['lang']}]({e['path']})")
            r["dates"] |= set(e["dates"])
        others = [e for e in es if e["kind"] != "leetcode"]
        out.append(f"### {emoji} {name}\n\n> **Signal:** {signal}  ·  *{len(lc)} LeetCode problems · {len(others)} concept lessons*\n")
        if lc:
            out.append("| # | Problem | Difficulty | Solution | Time | Solved Dates |\n|:-:|:--|:-:|:-:|:-:|:--|")
            for r in lc.values():
                cells = [
                    str(r["num"]),
                    link_name(r),
                    f"{DIFF_ICON.get(r['diff'], '🟡')} {r['diff']}",
                    " · ".join(r["files"]),
                    r.get("time", "O(n)").replace("|", "/"),
                    fmt_dates(r["dates"])
                ]
                out.append("| " + " | ".join(cells) + " |")
            out.append("")
        if others:
            out.append(f"<details><summary><b>📘 Lessons & Snippets ({len(others)})</b></summary>\n\n| What | Lang | Time | Dates |\n|:--|:-:|:-:|:--|")
            for o in sorted(others, key=lambda x: x["title"]):
                out.append(f"| [{o['title']}]({o['path']}) | {o['lang']} | {o.get('time', '—')} | {fmt_dates(o['dates'])} |")
            out.append("\n</details>\n")
    return "\n".join(out)


def build_repo_tree():
    lines = ["```text", "DSA-LeetCode-Journey/"]
    year_folders = [d for d in sorted(os.listdir(ROOT)) if re.match(r"^20\d\d$", d) and os.path.isdir(os.path.join(ROOT, d))]
    for yi, y in enumerate(year_folders):
        yp = os.path.join(ROOT, y)
        months = sorted(os.listdir(yp))
        lines.append(f"├── {y}/                           ← all practice solutions organized chronologically")
        for mi, m in enumerate(months):
            mp = os.path.join(yp, m)
            if os.path.isdir(mp):
                is_last_m = mi == len(months) - 1
                days_cnt = len([d for d in os.listdir(mp) if os.path.isdir(os.path.join(mp, d))])
                lines.append(f"│   {'└──' if is_last_m else '├──'} {m:<14} ({days_cnt} active days)")
    lines += [
        "├── notes/                        ← SQL deep dives & conceptual revision notes",
        "├── sandbox/                      ← Kafka and ML practice sandbox",
        "├── assets/                       ← generated banner, streak heatmap, RPG HUD, topic cards",
        "├── scripts/",
        "│   ├── build.py                  ← generates README + all SVGs from file headers",
        "│   └── new.py                    ← scaffold today's problem directly into yearly folders",
        "└── README.md                     ← gamified RPG dashboard + streak tracker + topic matrix",
        "```"
    ]
    return "\n".join(lines)



def write_site_data(entries, s):
    """Emit docs/problems.json for the GitHub Pages browser.

    The README can only ever be a static table. This feeds a page that can
    actually be searched and filtered across every solution in the repo.
    """
    docs = os.path.join(ROOT, "docs")
    os.makedirs(docs, exist_ok=True)

    items = []
    for e in entries:
        items.append({
            "num": e["num"],
            "title": e["title"] or os.path.basename(e["path"]),
            "difficulty": e["diff"] if e["kind"] == "leetcode" else "Lesson",
            "pattern": e["pattern"],
            "lang": e["lang"],
            "path": e["path"],
            "url": e["url"],
            "time": e.get("time", ""),
            "space": e.get("space", ""),
            "dates": [d.isoformat() for d in e["dates"]],
            "kind": e["kind"],
        })

    # Newest first, unnumbered lessons last within a date.
    items.sort(key=lambda x: (x["dates"][-1] if x["dates"] else "", x["num"] or 0), reverse=True)

    payload = {
        "generated": dt.datetime.now(TZ).isoformat(timespec="seconds"),
        "user": LEETCODE_USER,
        "repo": REPO,
        "stats": {
            "solved": s["solved_total"],
            "easy": s["easy"],
            "medium": s["medium"],
            "hard": s["hard"],
            "streak": s["current"],
            "longest": s["longest"],
            "active": s["active"],
            "rating": s["rating"],
            "topPct": s["top_pct"],
            "level": s["level"],
            "rank": s["rank_title"],
            "xp": s["xp"],
            "repoEntries": len(items),
        },
        "problems": items,
    }

    with open(os.path.join(docs, "problems.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(payload, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote docs/problems.json ({len(items)} entries)")


def main():
    print("Collecting solutions from dates/...")
    entries = collect_solutions()
    s = calculate_stats(entries)
    print(f"Loaded {len(entries)} solutions across {s['active']} days. Level {s['level']} {s['rank_title']}.")

    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    with open(os.path.join(ROOT, "assets", "banner.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(banner_svg(s))
    with open(os.path.join(ROOT, "assets", "streak.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(streak_svg(s))
    with open(os.path.join(ROOT, "assets", "rpg_card.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(rpg_card_svg(s))
    with open(os.path.join(ROOT, "assets", "topics.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(topics_svg(entries))
    print("Generated all 4 SVGs in assets/")

    write_site_data(entries, s)

    def achievement(have, target):
        """Badge cell that reflects the live number instead of a typed-in one."""
        if have >= target:
            return f"**UNLOCKED** ✅ ({have}/{target})"
        return f"🟡 In Progress ({have}/{target} · {round(have / target * 100)}%)"

    values = {
        "ACH_100": achievement(s["solved_total"], 100),
        "ACH_200": achievement(s["solved_total"], 200),
        "ACH_300": achievement(s["solved_total"], 300),
        "ACH_500": achievement(s["solved_total"], 500),
        "ACH_S30": achievement(s["current"], 30),
        "ACH_S50": achievement(s["current"], 50),
        "ACH_S100": achievement(s["current"], 100),
        "SOLVED": s["solved_total"],
        "EASY": s["easy"],
        "MEDIUM": s["medium"],
        "HARD": s["hard"],
        "CURRENT": s["current"],
        "LONGEST": s["longest"],
        "ACTIVE": s["active"],
        "LEVEL": s["level"],
        "RANK_TITLE": s["rank_title"],
        "XP": f"{s['xp']:,}",
        "PROGRESS": s["level_progress"],
        "RATING": s["rating"],
        "TOP_PCT": s["top_pct"],
        "CONTESTS": s.get("contests", 0),
        "GLOBAL_RANKING": f"{s.get('global_ranking', 0):,}",
        "TOTAL_PARTICIPANTS": f"{s.get('total_participants', 0):,}",
        "FETCHED_AT": s.get("fetched_at", ""),
        # Derived, so the milestone copy can never drift out of step again.
        "NEXT_MILESTONE": max(100, math.ceil((s["solved_total"] + 1) / 100) * 100),
        "REMAINING": max(0, math.ceil((s["solved_total"] + 1) / 100) * 100 - s["solved_total"]),
        "REPO_SOLVED": s["repo_solved"],
        "REPO_ENTRIES": s["repo_entries"],
        "TREE": build_repo_tree(),
        "BY_DATE": build_date_timeline(entries, s),
        "BY_TOPIC": build_topic_matrix(entries),
        "LEETCODE_USER": LEETCODE_USER,
        "REPO": REPO
    }

    tpl_path = os.path.join(ROOT, "scripts", "README.template.md")
    if os.path.exists(tpl_path):
        tpl = open(tpl_path, encoding="utf-8").read()
        readme = re.sub(r"\{\{(\w+)\}\}", lambda m: str(values.get(m[1], "")), tpl)
        with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(readme)
        print("README.md regenerated successfully!")


if __name__ == "__main__":
    main()
