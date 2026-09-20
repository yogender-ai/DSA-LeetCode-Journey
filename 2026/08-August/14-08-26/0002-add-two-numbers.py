"""
LeetCode 2 · Add Two Numbers · Medium
https://leetcode.com/problems/add-two-numbers/

Pattern : Math & Logic
Solved  : 14 Aug 2026
Time    : O(n)
Space   : O(1)
"""

# 2. Contains Duplicate
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
