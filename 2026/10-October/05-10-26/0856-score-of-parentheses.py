"""
LeetCode 856 · Score of Parentheses · Medium
https://leetcode.com/problems/score-of-parentheses/

Pattern : Stack
Solved  : 5 Oct 2026
Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
Space   : O(1) · Memory: 19.4 MB (Beats 17.1%)
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack=[0]
        for x in s:
            if x=="(":
                stack.append(0)
            else:
                inner=stack.pop()
                ans=max(2*inner,1)
                stack[-1]+=ans
        return stack[0]
