"""
LeetCode 3498 · Reverse Degree of a String · Easy
https://leetcode.com/problems/reverse-degree-of-a-string/

Pattern : Strings
Solved  : 20 Sep 2026
Time    : O(n) · Runtime: 11 ms (Beats 20.3%)
Space   : O(1) · Memory: 19.4 MB (Beats 19.1%)
"""

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for x in range(0,len(s)):
            q=26-(ord(s[x])-ord('a'))
            a=q*(x+1)
            ans+=a
        return ans
