/*
 * LeetCode 1480 · Running Sum of 1d Array · Easy
 * https://leetcode.com/problems/running-sum-of-1d-array/
 *
 * Pattern : Prefix Sum
 * Solved  : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int>prefixarray(nums.size());
        if(nums.size()>0){
            prefixarray[0]=nums[0];
            for(int i=1;i<nums.size();i++){
                prefixarray[i]=nums[i]+prefixarray[i-1];
                
            }
        }
        return prefixarray;
    }
};
