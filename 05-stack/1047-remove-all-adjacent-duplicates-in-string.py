"""
LeetCode 1047 · Remove All Adjacent Duplicates In String · Easy
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Pattern : Stack
Solved  : 19 Sep 2026
Time    : O(n^2) worst (list.pop(0) is O(n))
Space   : O(n)
Note    : Loop `for ch in s` instead of pop(0) and return ''.join(stack) for O(n).
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        l=list(s)
        stack=[]
        stack.append(l[0])
        l.pop(0)
        a=0
        ans=list()
        while len(l)!=0:
            if stack and l[0]==stack[-1] :
                stack.pop()
                l.pop(0)
            else:
                stack.append(l[0])
                l.pop(0)
        while stack:
            ans.append(stack[-1])
            stack.pop()
        ans.reverse()
        a="".join(ans)
        return a
