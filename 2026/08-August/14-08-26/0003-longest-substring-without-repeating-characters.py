"""
LeetCode 3 · Longest Substring Without Repeating Characters · Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern : Sliding Window
Solved  : 14 Aug 2026
Time    : O(n)
Space   : O(1)
"""

#3.  Valid Anagram
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
