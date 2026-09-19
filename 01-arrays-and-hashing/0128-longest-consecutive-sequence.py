"""
LeetCode 128 · Longest Consecutive Sequence · Medium
https://leetcode.com/problems/longest-consecutive-sequence/

Pattern : Sorting + linear scan
Solved  : 16 Aug 2026
Time    : O(n log n)
Space   : O(1) extra
Note    : A hash set lets you start only at sequence heads -> O(n).
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        start = nums[0]
        temp = 1

        for i in range(1, len(nums)):
            if start + 1 == nums[i]:
                temp += 1
            elif start == nums[i]:
                continue
            else:
                temp = 1
            start = nums[i]
            if temp > count:
                count = temp

        return count
