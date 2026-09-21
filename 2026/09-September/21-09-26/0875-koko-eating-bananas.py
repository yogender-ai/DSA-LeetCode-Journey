"""
LeetCode 875 · Koko Eating Bananas · Medium
https://leetcode.com/problems/koko-eating-bananas/

Pattern : Binary Search
Solved  : 21 Sep 2026
Time    : O(n) · Runtime: 173 ms (Beats 42.9%)
Space   : O(1) · Memory: 20.6 MB (Beats 44.9%)
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=[]
        while l<=r:
            mid = l+(r-l)//2
            count =0 
            for x in piles:
                a=math.ceil(x/mid)
                count+=a
            if count<=h:
                ans.append(mid)
                r=mid-1
            else:
                l=mid+1
        return min(ans)
