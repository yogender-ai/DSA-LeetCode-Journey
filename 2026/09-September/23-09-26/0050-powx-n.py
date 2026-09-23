"""
LeetCode 50 · Pow(x, n) · Medium
https://leetcode.com/problems/powx-n/

Pattern : Data Structures & Algorithms
Solved  : 23 Sep 2026
Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
Space   : O(1) · Memory: 12.4 MB (Beats 63.2%)
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        
        half= self.myPow(x,n//2)
        if n%2==0:
            return half*half 
        else:
            return half*half*x
