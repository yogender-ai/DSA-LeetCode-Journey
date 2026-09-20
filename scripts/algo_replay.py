"""Render an algorithm actually executing, as an animated SVG.

The steps are not hand-drawn. Each algorithm below is really run, and every
pointer move, comparison and window slide it makes is recorded as a frame.
The SVG is a flipbook of those frames, so what loops in the README is a
genuine execution trace rather than a decorative animation.

GitHub strips JavaScript from SVG but keeps CSS animations, so the flipbook
is driven by one @keyframes rule per frame toggling opacity.

    python scripts/algo_replay.py        # writes assets/algo_replay.svg
"""
import datetime as dt
import os
from xml.sax.saxutils import escape

TZ = dt.timezone(dt.timedelta(hours=5, minutes=30))  # IST

BG, PANEL, EDGE = "#05060f", "#0b0d1a", "#1e1b4b"
VIOLET, CYAN, PINK, LIME, AMBER, TEAL = "#8b5cf6", "#22d3ee", "#f472b6", "#a3e635", "#fbbf24", "#2dd4bf"
TEXT, MUTED, DIM = "#e2e8f0", "#94a3b8", "#475569"
SANS = "'Segoe UI','SF Pro Display',system-ui,-apple-system,sans-serif"
MONO = "'JetBrains Mono','Cascadia Code','SF Mono',Consolas,Menlo,monospace"

# state name -> (fill, stroke, text colour)
PALETTE = {
    "":      (PANEL, EDGE, MUTED),
    "range": ("#8b5cf618", "#8b5cf655", TEXT),
    "out":   ("#0b0d1a", "#12162e", "#2b3550"),
    "lo":    ("#22d3ee22", CYAN, TEXT),
    "hi":    ("#f472b622", PINK, TEXT),
    "mid":   ("#fbbf2426", AMBER, TEXT),
    "win":   ("#2dd4bf1f", "#2dd4bf88", TEXT),
    "hit":   ("#a3e63528", LIME, TEXT),
}


class Step:
    """One recorded moment of execution."""

    def __init__(self, state, note, stat="", marks=None):
        self.state = state          # list[str], one entry per array cell
        self.note = note            # what the algorithm just did
        self.stat = stat            # running value worth showing
        self.marks = marks or {}    # index -> pointer label, drawn above the cell


# ─────────────────────────── the algorithms ───────────────────────────
def trace_binary_search(arr, target):
    """Real binary search, recording the range it narrows to at each step."""
    steps = []
    lo, hi = 0, len(arr) - 1

    def snapshot(lo, hi, mid, note, stat):
        state = []
        for i in range(len(arr)):
            if i < lo or i > hi:
                state.append("out")
            elif i == mid:
                state.append("mid")
            elif i == lo:
                state.append("lo")
            elif i == hi:
                state.append("hi")
            else:
                state.append("range")
        marks = {lo: "lo", hi: "hi"}
        if mid is not None:
            marks[mid] = "mid"
        steps.append(Step(state, note, stat, marks))

    snapshot(lo, hi, None, f"Searching for {target} in a sorted array.", f"range = [{lo}, {hi}]  ·  {hi - lo + 1} candidates")

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            state = ["hit" if i == mid else "out" for i in range(len(arr))]
            steps.append(Step(state, f"arr[{mid}] == {target} — found it.", f"{len(steps)} comparisons, not {len(arr)}", {mid: "found"}))
            return steps
        if arr[mid] < target:
            snapshot(lo, hi, mid, f"arr[{mid}] = {arr[mid]} < {target} — discard the left half.", f"range = [{lo}, {hi}]  ·  {hi - lo + 1} candidates")
            lo = mid + 1
        else:
            snapshot(lo, hi, mid, f"arr[{mid}] = {arr[mid]} > {target} — discard the right half.", f"range = [{lo}, {hi}]  ·  {hi - lo + 1} candidates")
            hi = mid - 1

    steps.append(Step(["out"] * len(arr), f"{target} is not present.", "search space exhausted"))
    return steps


def trace_two_pointers(arr, target):
    """Two pointers converging on a pair that sums to target."""
    steps = []
    l, r = 0, len(arr) - 1
    while l < r:
        total = arr[l] + arr[r]
        state = []
        for i in range(len(arr)):
            if i < l or i > r:
                state.append("out")
            elif i == l:
                state.append("lo")
            elif i == r:
                state.append("hi")
            else:
                state.append("range")
        if total == target:
            state = ["hit" if i in (l, r) else "out" for i in range(len(arr))]
            steps.append(Step(state, f"{arr[l]} + {arr[r]} = {target} — pair found.", f"indices {l} and {r}", {l: "found", r: "found"}))
            return steps
        if total < target:
            note = f"{arr[l]} + {arr[r]} = {total} < {target} — too small, move left pointer right."
        else:
            note = f"{arr[l]} + {arr[r]} = {total} > {target} — too big, move right pointer left."
        steps.append(Step(state, note, f"sum = {total}", {l: "L", r: "R"}))
        if total < target:
            l += 1
        else:
            r -= 1
    steps.append(Step(["out"] * len(arr), "Pointers met — no pair sums to the target.", ""))
    return steps


def trace_sliding_window(arr, k):
    """Fixed-size window sliding once across the array, tracking the best sum."""
    steps = []
    window = sum(arr[:k])
    best, best_at = window, 0

    def snapshot(start, note, stat):
        state = []
        for i in range(len(arr)):
            if start <= i < start + k:
                state.append("win")
            else:
                state.append("")
        marks = {start: "start", start + k - 1: "end"}
        steps.append(Step(state, note, stat, marks))

    snapshot(0, f"First window of size {k} — sum it once, {k} additions.", f"sum = {window}  ·  best = {best}")

    for start in range(1, len(arr) - k + 1):
        leaving, entering = arr[start - 1], arr[start + k - 1]
        window += entering - leaving
        improved = ""
        if window > best:
            best, best_at = window, start
            improved = "  ← new best"
        snapshot(start, f"Slide: drop {leaving}, add {entering}. One subtraction, one addition — not {k}.", f"sum = {window}  ·  best = {best}{improved}")

    state = ["hit" if best_at <= i < best_at + k else "out" for i in range(len(arr))]
    steps.append(Step(state, f"Best window found in a single pass — O(n), not O(n·k).", f"max sum = {best} at index {best_at}", {best_at: "best"}))
    return steps


def trace_kadane(arr):
    """Kadane's: the running decision to extend or restart."""
    steps = []
    best = cur = arr[0]
    start = best_start = best_end = 0
    steps.append(Step(["win" if i == 0 else "" for i in range(len(arr))],
                      f"Start at {arr[0]}. Carry the best sum ending here.",
                      f"current = {cur}  ·  best = {best}", {0: "i"}))

    for i in range(1, len(arr)):
        prev = cur  # read before overwriting, or the note reports 0
        if prev + arr[i] < arr[i]:
            cur, start = arr[i], i
            note = f"{prev} + {arr[i]} = {prev + arr[i]} is worse than {arr[i]} alone — restart here."
        else:
            cur = prev + arr[i]
            note = f"{prev} + {arr[i]} = {cur} beats {arr[i]} alone — extend the run."
        improved = ""
        if cur > best:
            best, best_start, best_end = cur, start, i
            improved = "  ← new best"
        state = []
        for j in range(len(arr)):
            if start <= j <= i:
                state.append("win")
            elif best_start <= j <= best_end:
                state.append("range")
            else:
                state.append("")
        steps.append(Step(state, note, f"current = {cur}  ·  best = {best}{improved}", {i: "i"}))

    state = ["hit" if best_start <= i <= best_end else "out" for i in range(len(arr))]
    steps.append(Step(state, "One pass, no nested loop — O(n).", f"max subarray sum = {best}", {best_start: "best"}))
    return steps


# Each entry carries the array it runs on, so the data lives in exactly one
# place and the picture can never disagree with the trace.
ALGORITHMS = [
    {
        "num": 704, "name": "Binary Search", "slug": "binary-search",
        "pattern": "Binary Search", "complexity": "O(log n)",
        "values": [2, 5, 8, 12, 16, 23, 38, 47, 56, 72, 91],
        "build": lambda v: trace_binary_search(v, 12),
        "caption": "11 elements, 3 comparisons.",
    },
    {
        "num": 167, "name": "Two Sum II - Input Array Is Sorted", "slug": "two-sum-ii-input-array-is-sorted",
        "pattern": "Two Pointers", "complexity": "O(n)",
        "values": [2, 4, 7, 11, 15, 19, 24, 31],
        "build": lambda v: trace_two_pointers(v, 22),
        "caption": "No hash map, no nested loop.",
    },
    {
        "num": 643, "name": "Maximum Average Subarray I", "slug": "maximum-average-subarray-i",
        "pattern": "Sliding Window", "complexity": "O(n)",
        "values": [4, 2, 1, 7, 8, 1, 2, 8, 3, 9],
        "build": lambda v: trace_sliding_window(v, 4),
        "caption": "Each slide costs two operations, not k.",
    },
    {
        "num": 53, "name": "Maximum Subarray", "slug": "maximum-subarray",
        "pattern": "Dynamic Programming", "complexity": "O(n)",
        "values": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        "build": lambda v: trace_kadane(v),
        "caption": "Kadane's: extend or restart, nothing else.",
    },
]


def pick_algorithm(day=None):
    """Rotate daily, so the README is showing something different tomorrow."""
    day = day or dt.datetime.now(TZ).date()
    return ALGORITHMS[day.toordinal() % len(ALGORITHMS)]


# ───────────────────────────── rendering ─────────────────────────────
def _cells(step, values, x0, y, cw, gap):
    out = []
    for i in range(len(values)):
        fill, stroke, fg = PALETTE[step.state[i]]
        x = x0 + i * (cw + gap)
        out.append(
            f'<rect x="{x}" y="{y}" width="{cw}" height="{cw}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        )
        out.append(
            f'<text x="{x + cw / 2:.1f}" y="{y + cw / 2 + 6:.1f}" text-anchor="middle" '
            f'style="font:700 17px {MONO};fill:{fg}">{escape(str(values[i]))}</text>'
        )
        if i in step.marks:
            label = step.marks[i]
            colour = {"lo": CYAN, "L": CYAN, "start": TEAL, "hi": PINK, "R": PINK,
                      "end": TEAL, "mid": AMBER, "i": AMBER, "found": LIME, "best": LIME}.get(label, MUTED)
            out.append(
                f'<text x="{x + cw / 2:.1f}" y="{y - 12}" text-anchor="middle" '
                f'style="font:700 11px {MONO};letter-spacing:.8px;fill:{colour}">{escape(label)}</text>'
            )
            out.append(f'<path d="M{x + cw / 2:.1f} {y - 8} l-4 -5 h8 z" fill="{colour}"/>')
    return "".join(out)


def render(algo, values, solved_note=""):
    steps = algo["build"](values)
    n = len(values)
    W, H = 1200, 330
    cw, gap = min(62, (W - 160) // n - 8), 8
    row = n * cw + (n - 1) * gap
    x0 = (W - row) / 2
    y = 132

    per = 1.7  # seconds a frame stays on screen
    total = per * len(steps)

    frames, css = [], []
    for idx, s in enumerate(steps):
        a = idx / len(steps) * 100
        b = (idx + 1) / len(steps) * 100
        if idx == 0:
            css.append(f"@keyframes f{idx}{{0%,{b:.3f}%{{opacity:1}}{b + 0.001:.3f}%,100%{{opacity:0}}}}")
        else:
            css.append(
                f"@keyframes f{idx}{{0%,{a:.3f}%{{opacity:0}}{a + 0.001:.3f}%,{b:.3f}%{{opacity:1}}"
                f"{b + 0.001:.3f}%,100%{{opacity:0}}}}"
            )
        dots = "".join(
            f'<circle cx="{x0 + j * 16}" cy="{H - 34}" r="4" fill="{VIOLET if j == idx else EDGE}"/>'
            for j in range(len(steps))
        )
        frames.append(
            f'<g style="opacity:0;animation:f{idx} {total:.1f}s steps(1,end) infinite">'
            f'{_cells(s, values, x0, y, cw, gap)}'
            f'<text x="{x0}" y="{y + cw + 44}" style="font:500 16px {SANS};fill:{TEXT}">{escape(s.note)}</text>'
            f'<text x="{x0}" y="{y + cw + 70}" style="font:600 13px {MONO};fill:{MUTED}">{escape(s.stat)}</text>'
            f'<text x="{W - 56}" y="{H - 30}" text-anchor="end" style="font:700 12px {MONO};fill:{DIM}">'
            f'step {idx + 1}/{len(steps)}</text>'
            f'{dots}</g>'
        )

    title = f"#{algo['num']} · {algo['name']}"
    inner = f"""
<style>
  .tag{{font:700 12px {MONO};letter-spacing:2px;fill:{PINK}}}
  .ttl{{font:800 26px {SANS};fill:{TEXT}}}
  .sub{{font:600 13px {MONO};fill:{MUTED}}}
  .chip{{font:700 11px {MONO};letter-spacing:1px}}
  {chr(10).join("  " + c for c in css)}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="20" fill="{BG}" stroke="{EDGE}"/>
<rect x="28" y="24" width="{W - 56}" height="{H - 48}" rx="16" fill="{PANEL}" fill-opacity=".55" stroke="{EDGE}"/>
<text x="56" y="58" class="tag">// ALGORITHM REPLAY · REBUILT DAILY</text>
<text x="56" y="90" class="ttl">{escape(title)}</text>
<text x="56" y="112" class="sub">{escape(algo['pattern'])} · {escape(algo['complexity'])} · {escape(algo['caption'])}</text>
<g transform="translate({W - 56} 84)">
  <rect x="-150" y="-22" width="150" height="30" rx="15" fill="{VIOLET}" fill-opacity=".12" stroke="{VIOLET}" stroke-opacity=".5"/>
  <text x="-75" y="-2" text-anchor="middle" class="chip" fill="{VIOLET}">{escape(solved_note or 'LIVE TRACE')}</text>
</g>
{"".join(frames)}
"""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'role="img" aria-label="{escape(title)} executing step by step">'
        f"<title>{escape(title)} — animated execution trace</title>{inner}</svg>"
    )


def algo_replay_svg(entries=None, day=None):
    """Pick today's algorithm and render its trace.

    When the repo already contains a solution for that problem, the card says
    so, which keeps the card honest about what has actually been solved.
    """
    algo = pick_algorithm(day)
    values = algo["values"]

    solved_note = ""
    if entries:
        for e in entries:
            if e.get("kind") == "leetcode" and e.get("num") == algo["num"]:
                solved_note = "SOLVED IN THIS REPO"
                break
    return render(algo, values, solved_note)


if __name__ == "__main__":
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    os.makedirs(os.path.join(root, "assets"), exist_ok=True)
    out = os.path.join(root, "assets", "algo_replay.svg")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(algo_replay_svg())
    picked = pick_algorithm()
    print(f"wrote assets/algo_replay.svg — #{picked['num']} {picked['name']}")
