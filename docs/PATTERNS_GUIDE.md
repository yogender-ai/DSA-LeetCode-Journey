# Algorithmic Mastery & Pattern Cheatsheet 🧠

A field-tested distillation of fundamental algorithmic design patterns used across 276+ LeetCode problems.

---

## 1. Sliding Window (Two Pointers)
- **Signal**: Contiguous subarrays or substrings meeting a sum, length, or distinct character constraint.
- **Complexity**: Typically reduces brute force $O(N^2)$ to optimal $O(N)$ time, $O(1)$ space.
- **Mental Model**: Expand right pointer to satisfy constraint, shrink left pointer to minimize or restore invariant.

## 2. Monotonic Stack
- **Signal**: Next Greater Element, Next Smaller Element, Largest Rectangle in Histogram, Trapping Rain Water.
- **Complexity**: $O(N)$ time since each element enters and leaves the stack at most once.
- **Mental Model**: Keep elements in strictly increasing or decreasing order. Pop when invariant is violated.

## 3. Fast & Slow Pointers (Floyd's Cycle Finding)
- **Signal**: Linked lists or state arrays with potential cycles or finding the midpoint.
- **Complexity**: $O(N)$ time, $O(1)$ space.

## 4. Modified Binary Search
- **Signal**: Sorted or rotated arrays with $O(\log N)$ requirement.
- **Complexity**: $O(\log N)$ time, $O(1)$ space.
- **Key Check**: Determine which half is monotonically ordered before deciding left/right branch.

## 5. Dynamic Programming (State Transition)
- **Signal**: Overlapping subproblems and optimal substructure (knapsack, subsequences, grid paths).
- **Strategy**: Define $DP[i]$ precisely in human words before writing transition equation. Optimize space from $O(N^2)$ to $O(N)$ or $O(1)$ when only previous row/state is referenced.
