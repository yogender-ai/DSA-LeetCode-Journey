"""
LeetCode 1482 · Minimum Number of Days to Make m Bouquets · Medium
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

Pattern : Binary Search
Solved  : 21 Sep 2026
Time    : O(n) · Runtime: 290 ms (Beats 82.8%)
Space   : O(1) · Memory: 32.3 MB (Beats 43.8%)
"""

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        l=min(bloomDay)
        ans=[]
        r=max(bloomDay)
        while l<=r:
            mid=l+(r-l)//2
            a=0
            count=0
            for x in bloomDay:
                if x<=mid:
                    a+=1
                    if a==k:
                        count+=1
                        a=0
                else:
                    a=0
            if count>=m:
                r=mid-1
            else:
                l=mid+1
            
        return l
