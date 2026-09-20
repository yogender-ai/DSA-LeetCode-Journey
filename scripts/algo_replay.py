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
        "num": 1091, "name": "Shortest Path in Binary Matrix", "slug": "shortest-path-in-binary-matrix",
        "pattern": "Graphs & Search", "complexity": "O(rows · cols)",
        "kind": "grid", "values": None,
        "build": lambda v: trace_bfs_grid(),
        "caption": "Expands in rings, so first contact is already shortest.",
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
    """Lay out one algorithm's trace as a looping flipbook."""
    steps = algo["build"](values)
    grid = algo.get("kind") == "grid"
    W = 1200

    if grid:
        rows, cols = len(steps[0].state), len(steps[0].state[0])
        cell, gap = 26, 3
        span = cols * (cell + gap) - gap
        x0, y = (W - span) / 2, 128
        body_h = rows * (cell + gap) - gap
        note_y = y + body_h + 40
        H = note_y + 80
        left = x0
    else:
        n = len(values)
        cell, gap = min(62, (W - 160) // n - 8), 8
        span = n * cell + (n - 1) * gap
        x0, y = (W - span) / 2, 132
        note_y = y + cell + 44
        H = 330
        left = x0

    per = 1.4 if grid else 1.7
    total = per * len(steps)

    frames, css = [], []
    for idx, st in enumerate(steps):
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
            f'<circle cx="{left + j * 16}" cy="{H - 34}" r="4" fill="{VIOLET if j == idx else EDGE}"/>'
            for j in range(len(steps))
        )
        body = _grid(st, x0, y, cell, gap) if grid else _cells(st, values, x0, y, cell, gap)
        frames.append(
            f'<g style="opacity:0;animation:f{idx} {total:.1f}s steps(1,end) infinite">'
            f'{body}'
            f'<text x="{left}" y="{note_y}" style="font:500 16px {SANS};fill:{TEXT}">{escape(st.note)}</text>'
            f'<text x="{left}" y="{note_y + 26}" style="font:600 13px {MONO};fill:{MUTED}">{escape(st.stat)}</text>'
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
  <rect x="-170" y="-22" width="170" height="30" rx="15" fill="{VIOLET}" fill-opacity=".12" stroke="{VIOLET}" stroke-opacity=".5"/>
  <text x="-85" y="-2" text-anchor="middle" class="chip" fill="{VIOLET}">{escape(solved_note or 'LIVE TRACE')}</text>
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


# ───────────────────────── grid search (BFS) ─────────────────────────
GRID_PALETTE = {
    "wall":  ("#272160", "#3b3486"),
    "open":  ("#070912", "#191634"),
    "seen":  ("#8b5cf61f", "#8b5cf650"),
    "front": ("#22d3ee33", CYAN),
    "path":  ("#a3e63530", LIME),
    "S":     ("#fbbf2433", AMBER),
    "E":     ("#f472b633", PINK),
}

MAZE = [
    "S..#.........#.",
    ".#.#.#######.#.",
    ".#...#.....#.#.",
    ".#####.###.#.#.",
    ".....#.#...#.#.",
    "####.#.#.###.#.",
    ".....#...#....E",
]


def trace_bfs_grid(maze=None, stride=2):
    """Breadth-first search flooding a maze, one wave per frame.

    BFS is worth animating because the reason it finds the shortest path is
    visible: it expands in rings of equal distance, so the first time it
    touches the exit, no shorter route can exist.
    """
    maze = maze or MAZE
    rows, cols = len(maze), len(maze[0])
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "E":
                end = (r, c)

    def base():
        return [["wall" if maze[r][c] == "#" else "open" for c in range(cols)] for r in range(rows)]

    steps, parent = [], {start: None}
    frontier, seen, dist = [start], {start}, 0
    found = False

    # A 15-wide maze needs 20+ waves to cross, which would make a 40s loop.
    # Recording every `stride` waves keeps the flood readable and the loop short.
    while frontier and not found:
        if dist % stride and not found:
            pass
        state = base()
        for (r, c) in seen:
            state[r][c] = "seen"
        for (r, c) in frontier:
            state[r][c] = "front"
        state[start[0]][start[1]] = "S"
        state[end[0]][end[1]] = "E" if end not in seen else "front"
        if dist % stride == 0:
            steps.append(Step(state, f"Wave {dist}: every cell here is exactly {dist} step{'' if dist == 1 else 's'} from the start.",
                              f"frontier = {len(frontier)} cells  ·  visited = {len(seen)}"))

        nxt = []
        for (r, c) in frontier:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#" and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    nxt.append((nr, nc))
                    if (nr, nc) == end:
                        found = True
        frontier = nxt
        dist += 1

    # Walk the parent chain back to draw the shortest route.
    path, node = [], end
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()

    state = base()
    for (r, c) in seen:
        state[r][c] = "seen"
    for (r, c) in path:
        state[r][c] = "path"
    state[start[0]][start[1]] = "S"
    state[end[0]][end[1]] = "E"
    steps.append(Step(state, "First touch of the exit is already the shortest route - that is why BFS works.",
                      f"path length = {len(path) - 1} steps  ·  {len(seen)} of {rows * cols} cells explored"))
    return steps


def _grid(step, x0, y, cell, gap=3):
    out = []
    for r, row in enumerate(step.state):
        for c, st in enumerate(row):
            fill, stroke = GRID_PALETTE[st]
            x = x0 + c * (cell + gap)
            yy = y + r * (cell + gap)
            out.append(f'<rect x="{x:.1f}" y="{yy:.1f}" width="{cell}" height="{cell}" rx="5" '
                       f'fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
            if st in ("S", "E"):
                out.append(f'<text x="{x + cell / 2:.1f}" y="{yy + cell / 2 + 5:.1f}" text-anchor="middle" '
                           f'style="font:800 13px {MONO};fill:{AMBER if st == "S" else PINK}">{st}</text>')
    return "".join(out)
