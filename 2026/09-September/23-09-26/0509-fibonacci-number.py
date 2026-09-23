"""
LeetCode 509 · Fibonacci Number · Easy
https://leetcode.com/problems/fibonacci-number/

Pattern : Dynamic Programming
Solved  : 23 Sep 2026
Time    : O(n) · Runtime: 683 ms (Beats 7.4%)
Space   : O(1) · Memory: 12.5 MB (Beats 18.3%)
"""

class Solution(object):
    def fib(self, n):
        if n==0:
            return 0 
        if n==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)
