# Contributing to DSA & LeetCode Journey ⚔️

Welcome! This repository tracks daily algorithmic problem-solving with automated indexing, streak verification, and dynamic SVG HUD statistics.

---

## 📁 Repository Architecture

Solutions are structured chronologically by calendar date at the root:

```text
DSA-LeetCode-Journey/
├── 2025/
│   └── 07-July/
│       └── 14-07-25/
│           ├── solution.cpp
│           └── README.md
├── 2026/
│   └── 03-March/
│       └── 20-03-26/
│           ├── solution.py
│           └── README.md
├── scripts/
│   ├── build.py           # Rebuilds Topic Index, SVG Badges & README
│   ├── new.py             # Scaffolds today's problem template (<1ms)
│   └── questions_cache.json # Offline cache of 4,050+ LeetCode problems
└── assets/                # Dynamic SVG assets (HUD, Streak, Topics)
```

---

## ⚡ Quickstart: Adding a Solution

### 1. Scaffold Today's Problem
Run `new.py` with the LeetCode problem slug:

```bash
python scripts/new.py two-sum
```

This will:
- Determine today's date (`YYYY/MM-Month/DD-MM-YY`).
- Fetch the title, problem ID, topic tags, and difficulty from the offline cache.
- Generate standard starter templates in C++, Python, and an annotated `README.md`.

### 2. Implement Your Solution
Open the generated directory and write your optimal solution:
- Include time & space complexity annotations (`O(N)`, `O(1)`).
- Document edge cases and key pattern insights.

### 3. Rebuild Index & HUD
Run the automated build script to recalculate streaks, solve counts, topic distributions, and dynamic SVG badges:

```bash
python scripts/build.py
```

---

## 🎯 Code Quality Guidelines

- **Time & Space Complexity**: Always state the asymptotic complexity at the top of the file.
- **Variable Naming**: Use clear, descriptive names over single-letter shortcuts (except standard indices `i`, `j`, `k`).
- **Clean Formatting**: Format C++ with standard conventions and Python with PEP 8.
