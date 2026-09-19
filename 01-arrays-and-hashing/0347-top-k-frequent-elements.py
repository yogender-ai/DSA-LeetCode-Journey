"""
LeetCode 347 · Top K Frequent Elements · Medium
https://leetcode.com/problems/top-k-frequent-elements/

Pattern : Hash Map + Sort by frequency
Solved  : 16 Aug 2026
Time    : O(n log n)
Space   : O(n)
Note    : Bucket sort by frequency brings this to O(n).
"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1

        s = sorted(h.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for num in range(k):
            ans.append(s[num][0])
        return ans
