<div align="center">

# ⚔️ DSA · PYTHON ⚔️
### *The Algorithmic Battlefield*

```text
     ██████╗ ███████╗ █████╗ 
     ██╔══██╗██╔════╝██╔══██╗
     ██║  ██║███████╗███████║
     ██║  ██║╚════██║██╔══██║
     ██████╔╝███████║██║  ██║
     ╚═════╝ ╚══════╝╚═╝  ╚═╝
          ·  P Y T H O N  ·
```

**Not another problem dump.**  
This is a living war journal of how one mind learns to *think* in algorithms.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Grind-success?style=for-the-badge)](https://github.com/yogender-ai/DSA-Python-)
[![Mindset](https://img.shields.io/badge/Mindset-First%20Principles-blueviolet?style=for-the-badge)](#-the-philosophy)

</div>

---

### 🔥 Why this exists

Most DSA repositories are graveyards of copy-pasted solutions.  
This one is different by design.

Here every problem is treated as a **battle**:
- What is the *real* constraint?
- What mental model unlocks it?
- Why does this approach win on time *and* space?
- How would I explain it to a 5-year-old and to an interviewer in the same breath?

I am building this while preparing for real interviews (AIML + product companies).  
Every file, every comment, every complexity analysis is written with that pressure in mind.

> **Goal**: Reach a point where looking at a new problem feels less like panic and more like recognition.

---

### 🧠 The Philosophy (Read this before any code)

1. **Understand the shape of the problem first**  
   Arrays? Graph? DP state? Sliding window?  
   Name the pattern before writing a single line.

2. **Brute force is allowed — but only as a teacher**  
   Always write the O(n²) or O(2ⁿ) version in your head.  
   Only then ask: *Where is the waste?*

3. **Space is not free**  
   Hash maps are powerful. They are also a confession that you needed memory to buy time.  
   Sometimes the elegant solution uses O(1) extra space.

4. **Python is a double-edged sword**  
   Beautiful, expressive, dangerously slow if you abuse it.  
   Prefer clarity + correct complexity over micro-optimizations — until the interviewer asks.

5. **One problem ≠ one solution**  
   Every problem here will eventually have:
   - Brute
   - Better
   - Optimal
   - Edge-case notes
   - Interview talking points

---

### 🗂️ Current Structure

```text
DSA-Python-/
│
├── README.md                 ← You are here
├── Aug_14_2026.py            ← Day 1: Two Sum + Contains Duplicate
│
└── (future)
    ├── arrays/
    ├── hashing/
    ├── two-pointers/
    ├── sliding-window/
    ├── linked-list/
    ├── trees/
    ├── graphs/
    ├── dp/
    └── patterns/
```

---

### 📅 Daily Battle Log

| Date       | Problem                        | Status     | Approach                          | Complexity     | Notes |
|------------|--------------------------------|------------|-----------------------------------|----------------|-------|
| 14 Aug 2026 | Two Sum                       | ✅ Solved  | Sorted + Two Pointers (with index recovery) | O(n log n) time | Works but not optimal. Hash map version preferred for interviews |
| 14 Aug 2026 | Contains Duplicate            | ✅ Solved  | Hash Map frequency                | O(n) time / O(n) space | Clean. Can also be done with set |
| —          | *Next...*                     | 🔄         | —                                 | —              | —     |

---

### 🎯 Pattern Mastery Tracker

| Pattern              | Mastery | Key Problems |
|----------------------|---------|--------------|
| Hashing / Frequency  | 🟡      | Contains Duplicate, Two Sum |
| Two Pointers         | 🟡      | Two Sum (sorted) |
| Sliding Window       | ⚪      | — |
| Binary Search        | ⚪      | — |
| Linked List          | ⚪      | — |
| Trees (DFS/BFS)      | ⚪      | — |
| Graphs               | ⚪      | — |
| Dynamic Programming  | ⚪      | — |
| Greedy               | ⚪      | — |
| Backtracking         | ⚪      | — |

> Legend: ⚪ Not started · 🟡 In progress · 🟢 Comfortable · 🔥 Weaponized

---

### 🧬 How I solve (the actual process)

```text
1. Read the problem twice.
2. Write constraints + examples by hand.
3. Identify the pattern family.
4. Speak the brute force out loud.
5. Ask: "What information am I recomputing?"
6. Choose the data structure that removes that recomputation.
7. Code the clean version.
8. Dry-run on the example + one edge case.
9. Write time + space complexity *before* submitting.
10. After acceptance → write the "Why this works" comment.
```

This process is more important than any individual solution.

---

### 🚀 Roadmap (The Long War)

**Phase 1 — Foundations (Current)**  
Arrays · Hashing · Two Pointers · Sliding Window · Prefix Sum

**Phase 2 — Linear Structures**  
Linked Lists · Stacks · Queues · Monotonic Stack

**Phase 3 — Trees & Graphs**  
Binary Trees · BST · DFS/BFS · Topological Sort · Union-Find

**Phase 4 — Advanced**  
Dynamic Programming (1D → 2D → Knapsack → LIS) · Backtracking · Greedy proofs

**Phase 5 — Interview Simulation**  
Timed contests · Blind 75 / NeetCode 150 under pressure · System design light + DSA deep

---

### 💡 Code Style Rules in this repo

- Type hints everywhere
- Meaningful variable names (no `i`, `j`, `k` without context)
- Complexity comment at the top of every solution
- One clear approach per class (multiple approaches = multiple classes or clearly separated)
- Edge cases mentioned in comments when non-obvious

---

### 🤝 How to use this repo

1. Clone it.
2. Open any `.py` file.
3. Read the comments first — they contain the thinking.
4. Try to solve the problem yourself before looking at the code.
5. Compare your approach with mine.
6. Improve both.

---

<div align="center">

### *"The goal is not to remember solutions.  
The goal is to become the kind of person who can invent them."*

**Built with discipline by [Yogender](https://github.com/yogender-ai)**  
*Final year · AIML · LPU · Currently in the arena*

⭐ Star this repo if you also believe DSA is a skill of the mind, not of the fingers.

</div>
