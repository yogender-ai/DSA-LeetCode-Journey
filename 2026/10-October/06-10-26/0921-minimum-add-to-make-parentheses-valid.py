"""
LeetCode 921 · Minimum Add to Make Parentheses Valid · Medium
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Pattern : Stack
Solved  : 6 Oct 2026
Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
Space   : O(1) · Memory: 19.3 MB (Beats 15.6%)
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        ans = 0

        for ch in s:
            if ch == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    ans += 1

        return ans + open
