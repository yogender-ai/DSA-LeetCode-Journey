"""
LeetCode 20 · Valid Parentheses · Easy
https://leetcode.com/problems/valid-parentheses/

Pattern : Stack
Solved  : 7 Oct 2026
Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
Space   : O(1) · Memory: 19.3 MB (Beats 65.0%)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        t=0
        for x in s:
            if t==0:
                stack.append(x)
                t=1
            else:
                
                    if x == "(" or x == "{" or x == "[":
                        stack.append(x)
                    else:
                        if len(stack) == 0:
                            return False

                        a = stack[-1]

                        if x == ")" and a == "(":
                            stack.pop()
                        elif x == "}" and a == "{":
                            stack.pop()
                        elif x == "]" and a == "[":
                            stack.pop()
                        else:
                            return False
                
        if len(stack)==0:
            return True
        else:
            return False
