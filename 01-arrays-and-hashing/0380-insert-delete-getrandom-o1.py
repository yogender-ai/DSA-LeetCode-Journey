"""
LeetCode 380 · Insert Delete GetRandom O(1) · Medium
https://leetcode.com/problems/insert-delete-getrandom-o1/

Pattern : Hash Set (design)
Solved  : 12 Sep 2026
Time    : insert/remove O(1), getRandom O(n)
Space   : O(n)
Note    : list(set) is O(n); a list + index-map (swap with last on delete) makes getRandom O(1).
"""
import random

class RandomizedSet:
    def __init__(self):
        self.n = set()

    def insert(self, val: int) -> bool:
        if val in self.n:
            return False
        else:
            self.n.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.n:
            self.n.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.n))
