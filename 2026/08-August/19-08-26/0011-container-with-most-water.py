"""
LeetCode 11 · Container With Most Water · Medium
https://leetcode.com/problems/container-with-most-water/

Pattern : Two Pointers
Solved  : 19 Aug 2026
Time    : O(n)
Space   : O(1)
"""

#Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        mi=0
        ma=len(height)-1
        ans=0
        while mi<ma:
            a=min(height[mi],height[ma])
            temp=a*(ma-mi)
            if a==height[mi]:
                mi+=1
            else:
                ma-=1

            if temp>ans:
                ans=temp

        return ans
