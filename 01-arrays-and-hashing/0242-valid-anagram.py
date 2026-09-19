"""
LeetCode 242 · Valid Anagram · Easy
https://leetcode.com/problems/valid-anagram/

Pattern : Hashing / Counting
Solved  : 14 Aug 2026
Time    : O(n^2) (list.index + pop)
Space   : O(n)
Note    : Counting chars with a dict / Counter gives O(n).
"""
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w = list(t)
        for q in s:
            if q in w:
                ind = w.index(q)
                w.pop(ind)
            else:
                return False
        if not w:
            return True
        else:
            return False
