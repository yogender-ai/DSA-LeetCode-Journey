/*
 * LeetCode 342 · Power of Four · Easy
 * https://leetcode.com/problems/power-of-four/
 *
 * Pattern : Bit Manipulation
 * Solved  : 03 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n==1) return 1;
        if(n<4||n%4!=0)return 0;
        return isPowerOfFour(n/4);
    }
};
