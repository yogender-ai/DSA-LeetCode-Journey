"""Regenerate README.md + assets/*.svg from the headers inside every solution file.

    python scripts/build.py

Each file's header (LeetCode #, title, difficulty, pattern, time, Solved/Written/Date) is the single
source of truth. Topic view, date view, streaks and badges are all derived from it, so adding a file
(or running scripts/new.py) is enough — CI re-runs this on every push.
"""
import datetime as dt
import os
import re
from collections import Counter, OrderedDict, defaultdict
from xml.sax.saxutils import escape

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TZ = dt.timezone(dt.timedelta(hours=5, minutes=30))  # IST — decides what "today" is for the streak
REPO = "yogender-ai/DSA-LeetCode-Journey"

# folder -> (title, emoji, signal)
TOPICS = OrderedDict([
    ("01-arrays-and-hashing", ("Arrays & Hashing", "🧮", "\"have I seen this before?\", counting, grouping → **hash map / set**")),
    ("02-two-pointers", ("Two Pointers", "👉", "sorted input, pairs / triplets, palindromes → **shrink from both ends**")),
    ("03-sliding-window", ("Sliding Window", "🪟", "\"within k\", contiguous subarray → **grow right, shrink left**")),
    ("04-prefix-sum", ("Prefix Sum", "➕", "repeated range sums, \"split the array\" → **precompute prefix / suffix**")),
    ("05-stack", ("Stack", "📚", "\"cancel the previous one\", matching, nearest greater → **stack**")),
    ("06-strings", ("Strings & Pattern Matching", "🔤", "substrings, matching, compression → **two indices, LPS, run-length**")),
    ("07-sorting-and-stl", ("Sorting & STL", "🧰", "order matters, permutations → **sort / stable_sort / next_permutation**")),
    ("08-sql", ("SQL", "🗄️", "joins, grouping, windows → **think in sets, not loops**")),
    ("09-python-basics", ("Python Basics", "🐍", "the language warm-ups behind the Python solutions")),
])
LANG = {".py": "Python", ".cpp": "C++", ".sql": "SQL"}
DIFF_ICON = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

BG, PANEL, EDGE = "#05060f", "#0b0d1a", "#1e1b4b"
VIOLET, CYAN, PINK, LIME, AMBER, TEAL = "#8b5cf6", "#22d3ee", "#f472b6", "#a3e635", "#fbbf24", "#2dd4bf"
TEXT, MUTED, DIM = "#e2e8f0", "#94a3b8", "#475569"
LEVELS = ["#161b33", "#3b1f7a", "#6d28d9", "#8b5cf6", "#c4b5fd"]
SANS = "'Segoe UI', 'SF Pro Display', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Cascadia Code', 'SF Mono', Consolas, Menlo, monospace"


# ─────────────────────────────── parsing ───────────────────────────────
def parse(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    with open(path, encoding="utf-8") as f:
        head = [re.sub(r'^\s*(/\*+|\*/|\*|--|#|""")?\s?', "", l).rstrip() for l in f.read().splitlines()[:16]]
    text = "\n".join(head)
    e = {"path": rel, "topic": rel.split("/")[0], "lang": LANG[os.path.splitext(path)[1]], "num": None,
         "title": None, "diff": None, "pattern": "", "time": "", "dates": [], "kind": "snippet"}
    m = re.search(r"LeetCode (\d+) · (.+?) · (Easy|Medium|Hard)", text)
    if m:
        e.update(kind="leetcode", num=int(m[1]), title=m[2], diff=m[3])
        u = re.search(r"https://leetcode\.com/problems/[\w-]+/", text)
        e["url"] = u[0] if u else None
    elif re.search(r"SQL Lesson (\d+) · (.+)", text):
        m = re.search(r"SQL Lesson (\d+) · (.+)", text)
        e.update(kind="lesson", num=int(m[1]), title=m[2], path=rel.rsplit("/", 1)[0] + "/")
    else:
        e["title"] = next((l for l in head if l and not re.match(r"(Written|Solved|Date|Time|Run)\b", l)), rel)
    for key, rx in (("pattern", r"Pattern\s*:\s*(.+)"), ("time", r"Time\s*:\s*(.+)")):
        m = re.search(rx, text)
        if m:
            e[key] = m[1].strip()
    m = re.search(r"(?:Solved|Written|Date)\s*:\s*(.+)", text)
    if m:
        for part in m[1].split(","):
            try:
                e["dates"].append(dt.datetime.strptime(part.strip(), "%d %b %Y").date())
            except ValueError:
                pass
    return e


def collect():
    out = []
    for topic in TOPICS:
        for dp, _, files in os.walk(os.path.join(ROOT, topic)):
            for fn in sorted(files):
                if os.path.splitext(fn)[1] in LANG:
                    e = parse(os.path.join(dp, fn))
                    if e["kind"] != "snippet" or e["dates"]:
                        out.append(e)
    return out


# ─────────────────────────────── stats ─────────────────────────────────
def stats(entries):
    days = Counter(d for e in entries for d in e["dates"])
    ds = sorted(days)
    today = dt.datetime.now(TZ).date()
    longest, best_end, run = 0, None, 0
    for i, d in enumerate(ds):
        run = run + 1 if i and (d - ds[i - 1]).days == 1 else 1
        if run > longest:
            longest, best_end = run, d
    cur, d = 0, today if today in days else today - dt.timedelta(days=1)
    while d in days:
        cur, d = cur + 1, d - dt.timedelta(days=1)
    uniq = {}
    for e in entries:
        if e["kind"] == "leetcode":
            uniq[e["num"]] = e["diff"]
    last = max(((d, e) for e in entries for d in e["dates"]), key=lambda x: (x[0], x[1]["kind"] == "leetcode"))
    return dict(days=days, first=ds[0], last_day=ds[-1], today=today, current=cur, longest=longest,
                best=(best_end - dt.timedelta(days=longest - 1), best_end), active=len(ds),
                solved=len(uniq), diff=Counter(uniq.values()), last=last,
                langs=sorted({e["lang"] for e in entries}))


# ─────────────────────────────── SVGs ──────────────────────────────────
def svg(w, h, inner, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
            f'aria-label="{escape(title)}"><title>{escape(title)}</title>{inner}</svg>\n')


def banner(s):
    import random
    rnd = random.Random(3)
    W, H = 1200, 300
    tokens = ["O(n)", "{ }", "[i, j]", "dp[i]", "while l < r", "hash[x]++", "O(log n)", "stack.pop()", "∑", "→",
              "JOIN", "GROUP BY", "lps[i]", "prefix[i]", "O(1)", "set()", "window", "sort()", "3Sum", "two ptr"]
    floats = "".join(
        f'<text x="{rnd.randint(30, W - 90)}" y="{H + 20}" class="tk" style="animation-duration:{rnd.uniform(9, 16):.1f}s;'
        f'animation-delay:-{rnd.uniform(0, 16):.1f}s;font-size:{rnd.choice([12, 14, 16, 18])}px" fill="{rnd.choice([VIOLET, CYAN, PINK, MUTED])}">'
        f'{escape(t)}</text>' for t in tokens * 2)
    lines = [f"{s['solved']} problems · {s['active']} practice days · {len(s['langs'])} languages",
             "organised by topic — and by date", f"longest streak: {s['longest']} days · current: {s['current']}",
             "one problem a day"]
    roll = "".join(f'<text x="600" y="214" class="rl" style="animation-delay:{i * 3}s">{escape(t)}</text>' for i, t in enumerate(lines))
    inner = f"""
<defs>
  <linearGradient id="g" x1="0" x2="1" spreadMethod="reflect"><stop offset="0" stop-color="{VIOLET}"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{PINK}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1 0;0 0" dur="7s" repeatCount="indefinite"/></linearGradient>
  <filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="50"/></filter>
  <clipPath id="c"><rect width="{W}" height="{H}" rx="24"/></clipPath>
</defs>
<style>
  .tk{{font-family:{MONO};opacity:0;animation:up linear infinite}}
  @keyframes up{{0%{{transform:translateY(0);opacity:0}}15%{{opacity:.16}}85%{{opacity:.16}}100%{{transform:translateY(-{H + 60}px);opacity:0}}}}
  .t{{font:800 64px {SANS};text-anchor:middle;letter-spacing:2px}} .k{{font:700 14px {MONO};letter-spacing:6px;fill:{MUTED};text-anchor:middle}}
  .rl{{font:500 20px {MONO};fill:{CYAN};text-anchor:middle;opacity:0;animation:rl 12s infinite}}
  @keyframes rl{{0%{{opacity:0;transform:translateY(12px)}}3%,22%{{opacity:1;transform:none}}25%,100%{{opacity:0;transform:translateY(-12px)}}}}
  .o1{{animation:o1 12s ease-in-out infinite}} .o2{{animation:o2 15s ease-in-out infinite}}
  @keyframes o1{{50%{{transform:translate(220px,40px)}}}} @keyframes o2{{50%{{transform:translate(-240px,-30px)}}}}
</style>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g filter="url(#b)" opacity=".7"><circle class="o1" cx="250" cy="110" r="150" fill="{VIOLET}"/><circle class="o2" cx="950" cy="190" r="150" fill="{CYAN}" opacity=".7"/></g>
  {floats}
  <text x="600" y="92" class="k">// DATA STRUCTURES &amp; ALGORITHMS</text>
  <rect x="150" y="100" width="900" height="130" rx="30" fill="{BG}" opacity=".55" filter="url(#b)"/>
  <text x="600" y="164" class="t" fill="url(#g)">DSA · LeetCode Journey</text>
  {roll}
</g>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="24" fill="none" stroke="{EDGE}"/>
"""
    return svg(W, H, inner, "DSA · LeetCode Journey")


def streak_card(s):
    W, H = 1200, 400
    start = s["first"] - dt.timedelta(days=(s["first"].isoweekday() % 7))
    end = max(s["today"], s["last_day"])
    weeks = (end - start).days // 7 + 1
    cell = min(15.0, (W - 80) / weeks - 4)
    step = cell + 4
    x0 = (W - weeks * step) / 2 + 2
    y0, mx = 200, max(s["days"].values())
    cells, months = [], []
    d = start
    while d <= end:
        wi, wd = (d - start).days // 7, d.isoweekday() % 7
        c = s["days"].get(d, 0)
        lvl = 0 if c == 0 else min(4, 1 + round(3 * (c - 1) / max(mx - 1, 1)))
        tip = f"{d:%d %b %Y}: {c} solved" if c else f"{d:%d %b %Y}"
        extra = ' class="on" style="animation-delay:%.2fs"' % (wi * .05) if c else ""
        cells.append(f'<rect x="{x0 + wi * step:.1f}" y="{y0 + wd * step:.1f}" width="{cell:.1f}" height="{cell:.1f}" rx="3" fill="{LEVELS[lvl]}"'
                     f'{extra}><title>{tip}</title></rect>')
        if d.day == 1 or d == start:
            months.append(f'<text x="{x0 + wi * step:.1f}" y="{y0 - 10}" class="m">{d:%b}{" ’" + d.strftime("%y") if d.month == 1 or d == start else ""}</text>')
        d += dt.timedelta(days=1)
    b0, b1 = s["best"]
    tiles = [("🔥 CURRENT STREAK", f"{s['current']}", ("day" if s["current"] == 1 else "days") + " in a row" if s["current"] else "solve one today to start", LIME),
             ("🏆 LONGEST STREAK", f"{s['longest']}", f"{b0:%d %b} → {b1:%d %b %Y}", AMBER),
             ("📅 PRACTICE DAYS", f"{s['active']}", f"since {s['first']:%b %Y}", CYAN),
             ("✅ SOLVED", f"{s['solved']}", f"{s['diff']['Easy']} easy · {s['diff']['Medium']} medium · {s['diff']['Hard']} hard", VIOLET)]
    t = "".join(f'<g transform="translate({32 + i * 288} 28)"><rect width="272" height="112" rx="14" fill="{c}" fill-opacity=".07" stroke="{c}" stroke-opacity=".35"/>'
                f'<text x="18" y="30" class="lb" fill="{c}">{l}</text><text x="18" y="76" class="big">{v}</text><text x="18" y="98" class="sub">{escape(sb)}</text></g>'
                for i, (l, v, sb, c) in enumerate(tiles))
    legend = "".join(f'<rect x="{W - 170 + i * 19}" y="{H - 34}" width="14" height="14" rx="3" fill="{c}"/>' for i, c in enumerate(LEVELS))
    inner = f"""
<style>
  .lb{{font:700 12px {MONO};letter-spacing:1.5px}} .big{{font:800 40px {SANS};fill:{TEXT}}} .sub{{font:500 13px {SANS};fill:{MUTED}}}
  .m{{font:600 11px {MONO};fill:{MUTED}}} .u{{font:500 11px {MONO};fill:{DIM}}}
  .on{{animation:pop 5s ease-in-out infinite}} @keyframes pop{{0%,80%,100%{{opacity:1}}88%{{opacity:.4}}}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{PANEL}" stroke="{EDGE}"/>
{t}
{''.join(months)}
{''.join(cells)}
<text x="32" y="{H - 22}" class="u">every square = a day I solved something · updated {s['today']:%d %b %Y}</text>
<text x="{W - 205}" y="{H - 22}" class="u">less</text>{legend}<text x="{W - 72}" y="{H - 22}" class="u">more</text>
"""
    return svg(W, H, inner, f"Streak: {s['current']} current, {s['longest']} longest, {s['active']} practice days")


def topics_card(entries):
    W = 1200
    rows = []
    for folder, (name, emoji, _) in TOPICS.items():
        es = [e for e in entries if e["topic"] == folder]
        if not es:
            continue
        seen, c = set(), Counter()
        for e in es:
            k = (e["kind"], e["num"], e["title"])
            if k in seen:
                continue
            seen.add(k)
            c[e["diff"] if e["kind"] == "leetcode" else "Other"] += 1
        rows.append((f"{emoji} {name}", c))
    mx = max(sum(c.values()) for _, c in rows)
    H = 70 + len(rows) * 34 + 30
    cols = [("Easy", TEAL), ("Medium", AMBER), ("Hard", PINK), ("Other", VIOLET)]
    out = []
    for i, (label, c) in enumerate(rows):
        y, x = 64 + i * 34, 330
        out.append(f'<text x="40" y="{y + 14}" class="l">{escape(label)}</text><rect x="330" y="{y}" width="760" height="18" rx="9" fill="{EDGE}" fill-opacity=".6"/>')
        for k, col in cols:
            if c[k]:
                w = 760 * c[k] / mx
                out.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w - 2, 4):.1f}" height="18" rx="9" fill="{col}" class="gr" style="animation-duration:{.8 + i * .12:.2f}s"/>')
                x += w
        out.append(f'<text x="{x + 10:.0f}" y="{y + 14}" class="n">{sum(c.values())}</text>')
    lg = "".join(f'<circle cx="{40 + i * 150}" cy="{H - 22}" r="6" fill="{col}"/><text x="{52 + i * 150}" y="{H - 17}" class="s">'
                 f'{"lessons / snippets" if k == "Other" else k}</text>' for i, (k, col) in enumerate(cols))
    inner = f"""
<style>
  .l{{font:600 15px {SANS};fill:{TEXT}}} .n{{font:700 13px {MONO};fill:{MUTED}}} .s{{font:500 13px {SANS};fill:{MUTED}}}
  .h{{font:700 13px {MONO};letter-spacing:3px;fill:{VIOLET}}}
  .gr{{transform-box:fill-box;transform-origin:left;animation:gr 1s cubic-bezier(.2,.8,.2,1)}} @keyframes gr{{from{{transform:scaleX(0)}}}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{PANEL}" stroke="{EDGE}"/>
<text x="40" y="38" class="h">// PROBLEMS PER TOPIC</text>
{''.join(out)}{lg}
"""
    return svg(W, H, inner, "Problems per topic")


# ─────────────────────────────── markdown ──────────────────────────────
def link_name(e):
    if e["kind"] == "leetcode" and e.get("url"):
        return f"[{e['title']}]({e['url']})"
    return f"[{e['title']}]({e['path']})"


def fmt_dates(ds):
    return ", ".join(f"{d:%d %b %Y}" for d in sorted(ds))


def topic_section(entries):
    out = []
    for folder, (name, emoji, signal) in TOPICS.items():
        es = [e for e in entries if e["topic"] == folder]
        if not es:
            continue
        lc = OrderedDict()
        for e in sorted((e for e in es if e["kind"] == "leetcode"), key=lambda e: e["num"]):
            r = lc.setdefault(e["num"], dict(e, files=[], dates=set()))
            r["files"].append(f"[{e['lang']}]({e['path']})")
            r["dates"] |= set(e["dates"])
            r["pattern"] = r["pattern"] or e["pattern"]
            r["time"] = r["time"] or e["time"]
        others = [e for e in es if e["kind"] != "leetcode"]
        out.append(f"### {emoji} {name}\n\n> **Signal:** {signal}  ·  📁 [`{folder}/`]({folder})\n")
        if lc:
            rows = list(lc.values())
            show_p = any(r["pattern"] for r in rows)
            show_t = any(r["time"] for r in rows)
            hdr = ["#", "Problem", "Difficulty"] + (["Pattern"] if show_p else []) + ["Solution"] + (["Time"] if show_t else []) + ["Solved"]
            out.append("| " + " | ".join(hdr) + " |\n|" + "|".join([":-:", ":--", ":-:"] + ([":--"] if show_p else []) + [":-:"] + ([":-:"] if show_t else []) + [":--"]) + "|")
            for r in rows:
                cells = [str(r["num"]), link_name(r), f"{DIFF_ICON[r['diff']]} {r['diff']}"] + ([r["pattern"]] if show_p else []) + \
                        [" · ".join(r["files"])] + ([r["time"].replace("|", "/")] if show_t else []) + [fmt_dates(r["dates"])]
                out.append("| " + " | ".join(cells) + " |")
            out.append("")
        if others:
            label = "📘 Lessons" if others[0]["kind"] == "lesson" else "🧩 Concept snippets"
            out.append(f"<details><summary><b>{label} ({len(others)})</b></summary>\n\n| What | Lang | Time | Written |\n|:--|:-:|:-:|:--|")
            for e in sorted(others, key=lambda e: (e["num"] or 0, e["title"])):
                title = f"Lesson {e['num']:02d} · {e['title']}" if e["kind"] == "lesson" else e["title"]
                out.append(f"| [{title}]({e['path']}) | {e['lang']} | {e['time'] or '—'} | {fmt_dates(e['dates'])} |")
            out.append("\n</details>\n")
    return "\n".join(out)


def date_section(entries, s):
    by_day = defaultdict(list)
    for e in entries:
        ds = sorted(e["dates"])
        for i, d in enumerate(ds):
            by_day[d].append((e, i > 0))
    months = OrderedDict()
    for d in sorted(by_day, reverse=True):
        months.setdefault((d.year, d.month), []).append(d)
    # overview tree with bars
    tree = ["```text", "📅 journey/"]
    years = OrderedDict()
    for (y, m), ds in months.items():
        years.setdefault(y, []).append((m, ds))
    mx = max(sum(len(by_day[d]) for d in ds) for ds in months.values())
    for yi, (y, ms) in enumerate(years.items()):
        last_y = yi == len(years) - 1
        n_y = sum(len(by_day[d]) for _, ds in ms for d in ds)
        tree.append(f"{'└──' if last_y else '├──'} {y}/  ·  {n_y} entries · {sum(len(ds) for _, ds in ms)} days")
        for mi, (m, ds) in enumerate(ms):
            n = sum(len(by_day[d]) for d in ds)
            bar = "█" * max(1, round(20 * n / mx))
            pre = "    " if last_y else "│   "
            tree.append(f"{pre}{'└──' if mi == len(ms) - 1 else '├──'} {dt.date(y, m, 1):%b}  {bar:<20}  {n:>2} entr{'ies' if n != 1 else 'y '} · {len(ds)} day{'s' if len(ds) > 1 else ''}")
    tree.append("```")

    out = ["\n".join(tree), ""]
    for i, ((y, m), ds) in enumerate(months.items()):
        n = sum(len(by_day[d]) for d in ds)
        out.append(f"<details{' open' if i == 0 else ''}>\n<summary><b>{dt.date(y, m, 1):%B %Y}</b> — {n} entr{'ies' if n != 1 else 'y'} on {len(ds)} day{'s' if len(ds) > 1 else ''}</summary>\n")
        out.append("| Day | Solved / studied | Topic | Level |\n|:--|:--|:--|:-:|")
        for d in ds:
            items = sorted(by_day[d], key=lambda x: (x[0]["kind"] != "leetcode", x[0]["topic"], x[0]["num"] or 0))
            for j, (e, revisit) in enumerate(items):
                day = f"**{d:%d}** {d:%a}" if j == 0 else ""
                name = (f"{e['num']}. " if e["kind"] == "leetcode" else "") + link_name(e) + (" ↺ *revisit*" if revisit else "")
                if e["kind"] == "leetcode":
                    name += f" · [{e['lang']}]({e['path']})"
                lvl = DIFF_ICON.get(e["diff"], "📘" if e["kind"] == "lesson" else "🧩")
                out.append(f"| {day} | {name} | {TOPICS[e['topic']][1]} {TOPICS[e['topic']][0]} | {lvl} |")
        out.append("\n</details>\n")
    return "\n".join(out)


def repo_tree(entries):
    lines = ["```text", "DSA-LeetCode-Journey/"]
    folders = [f for f in TOPICS if os.path.isdir(os.path.join(ROOT, f))] + ["10-sandbox"]
    for i, f in enumerate(folders):
        es = [e for e in entries if e["topic"] == f]
        lc = len({e["num"] for e in es if e["kind"] == "leetcode"})
        other = len([e for e in es if e["kind"] != "leetcode"])
        note = " · ".join(x for x in [f"{lc} problems" if lc else "", f"{other} {'lessons' if f == '08-sql' else 'snippets'}" if other else ""] if x) or "experiments"
        lines.append(f"{'└──' if i == len(folders) - 1 else '├──'} {f + '/':<26} {TOPICS.get(f, ('', '🧪'))[1]}  {note}")
    lines += ["", "scripts/build.py   ← regenerates this README + all SVGs from the file headers",
              "scripts/new.py     ← scaffold today's problem:  python scripts/new.py two-sum 01", "```"]
    return "\n".join(lines)


def main():
    entries = collect()
    s = stats(entries)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    for name, body in (("banner.svg", banner(s)), ("streak.svg", streak_card(s)), ("topics.svg", topics_card(entries))):
        with open(os.path.join(ROOT, "assets", name), "w", encoding="utf-8", newline="\n") as f:
            f.write(body)
    d, e = s["last"]
    last = (f"{e['num']}. " if e["kind"] == "leetcode" else "") + link_name(e)
    values = {
        "SOLVED": s["solved"], "EASY": s["diff"]["Easy"], "MEDIUM": s["diff"]["Medium"], "HARD": s["diff"]["Hard"],
        "CURRENT": s["current"], "LONGEST": s["longest"], "ACTIVE": s["active"],
        "LAST": f"{last} · {d:%d %b %Y}", "REPO": REPO,
        "TREE": repo_tree(entries), "BY_TOPIC": topic_section(entries), "BY_DATE": date_section(entries, s),
    }
    tpl = open(os.path.join(ROOT, "scripts", "README.template.md"), encoding="utf-8").read()
    readme = re.sub(r"\{\{(\w+)\}\}", lambda m: str(values[m[1]]), tpl)
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(readme)
    print(f"README + assets rebuilt · {len(entries)} entries · {s['solved']} solved · streak {s['current']} / best {s['longest']}")


if __name__ == "__main__":
    main()
