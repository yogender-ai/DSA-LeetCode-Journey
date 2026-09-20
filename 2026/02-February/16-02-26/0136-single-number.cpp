/*
 * LeetCode 136 · Single Number · Easy
 * https://leetcode.com/problems/single-number/
 *
 * Pattern : Bit Manipulation
 * Solved  : 16 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans=0;
        for( int x:nums){
            ans^=x;
        }
        return ans;
    }
};
