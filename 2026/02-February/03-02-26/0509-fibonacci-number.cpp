/*
 * LeetCode 509 · Fibonacci Number · Easy
 * https://leetcode.com/problems/fibonacci-number/
 *
 * Pattern : Dynamic Programming
 * Solved  : 03 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int fib(int n) {
        if(n==0) return n;
        if(n==1) return n;
        return (fib(n-1)+fib(n-2));
        
    }
};
