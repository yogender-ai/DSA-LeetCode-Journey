/*
 * LeetCode 55 · Jump Game · Medium
 * https://leetcode.com/problems/jump-game/
 *
 * Pattern : Dynamic Programming
 * Solved  : 08 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    
    bool canJump(vector<int>& nums) {
       int f=0;
       for(int i=0;i<nums.size();i++){
        if(i>f) return 0;
        f=max(f,i+nums[i]);
       }
       return 1;
    }
};
