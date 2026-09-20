/*
 * LeetCode 191 · Number of 1 Bits · Easy
 * https://leetcode.com/problems/number-of-1-bits/
 *
 * Pattern : Bit Manipulation
 * Solved  : 16 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int hammingWeight(int n) {
        int a=0;
        while(n){
            n=n&(n-1);
            a++;
        }
        return a;
        
    }
};
