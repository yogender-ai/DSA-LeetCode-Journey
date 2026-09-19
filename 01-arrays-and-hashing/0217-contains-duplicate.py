"""
LeetCode 217 · Contains Duplicate · Easy
https://leetcode.com/problems/contains-duplicate/

Pattern : Hash Map (frequency)
Solved  : 14 Aug 2026
Time    : O(n)
Space   : O(n)
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
                return True
            else:
                count[num] = 1
        return False
