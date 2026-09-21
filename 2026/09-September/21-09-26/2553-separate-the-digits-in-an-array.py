"""
LeetCode 2553 · Separate the Digits in an Array · Easy
https://leetcode.com/problems/separate-the-digits-in-an-array/

Pattern : Data Structures & Algorithms
Solved  : 21 Sep 2026
Time    : O(n) · Runtime: 3 ms (Beats 73.1%)
Space   : O(1) · Memory: 19.3 MB (Beats 97.6%)
"""

class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        a=str(nums)
        return  [int(x) for x in a if x.isdigit()]
