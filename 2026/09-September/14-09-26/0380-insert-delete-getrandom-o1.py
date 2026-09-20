"""
LeetCode 380 · Insert Delete GetRandom O(1) · Medium
https://leetcode.com/problems/insert-delete-getrandom-o1/

Pattern : Arrays & Hashing
Solved  : 12 Sep 2026
Time    : O(n)
Space   : O(1)
"""

# 380. Insert Delete GetRandom O(1)
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
