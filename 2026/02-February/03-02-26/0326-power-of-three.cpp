/*
 * LeetCode 326 · Power of Three · Easy
 * https://leetcode.com/problems/power-of-three/
 *
 * Pattern : Math & Logic
 * Solved  : 03 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n==1) return 1;
        if(n<1||n%3!=0) return 0;
        return isPowerOfThree(n/3);
        
    }
};
