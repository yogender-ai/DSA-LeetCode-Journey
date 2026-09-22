"""
LeetCode 1283 · Find the Smallest Divisor Given a Threshold · Medium
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Pattern : Binary Search
Solved  : 22 Sep 2026
Time    : O(n) · Runtime: 139 ms (Beats 35.8%)
Space   : O(1) · Memory: 24.4 MB (Beats 39.9%)
"""

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
     l=1
     r=max(nums)
     ans=[]
     while l<=r:
        mid=l+(r-l)//2
        sum=0
        for x in nums:
            a=math.ceil(x/mid)
            sum+=a
        
        if sum<=threshold:
            ans.append(mid)
            r=mid-1
            
        else:
            l=mid+1
     
     
     if len(ans)!=0:
        return min(ans)
     else:
        return 0
