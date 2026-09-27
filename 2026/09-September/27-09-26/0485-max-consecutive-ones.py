"""
LeetCode 485 · Max Consecutive Ones · Easy
https://leetcode.com/problems/max-consecutive-ones/

Pattern : Data Structures & Algorithms
Solved  : 27 Sep 2026
Time    : O(n) · Runtime: 7 ms (Beats 96.5%)
Space   : O(1) · Memory: 21.9 MB (Beats 44.6%)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        ans = []

        for x in nums:
            if x == 1:
                a += 1
            else:
                ans.append(a)
                a = 0

        ans.append(a)

        return max(ans)
