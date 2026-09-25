"""
LeetCode 674 · Longest Continuous Increasing Subsequence · Easy
https://leetcode.com/problems/longest-continuous-increasing-subsequence/

Pattern : Data Structures & Algorithms
Solved  : 25 Sep 2026
Time    : O(n) · Runtime: 4 ms (Beats 19.2%)
Space   : O(1) · Memory: 20.4 MB (Beats 84.5%)
"""

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        count = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                count = 1

            ans = max(ans, count)

        return ans
