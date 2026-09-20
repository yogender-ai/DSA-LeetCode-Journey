/*
 * LeetCode 90 · Subsets II · Medium
 * https://leetcode.com/problems/subsets-ii/
 *
 * Pattern : Bit Manipulation
 * Solved  : 09 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    void help(vector<vector<int>>&ans,vector<int>&curr,vector<int>&nums,int i){
        if(i==nums.size()){
            ans.push_back(curr);
            return;
        }
        curr.push_back(nums[i]);
        help(ans,curr,nums,i+1);
        curr.pop_back();
        while (i + 1 < nums.size() && nums[i] == nums[i + 1]) {
            i++;
        }
        help(ans,curr,nums,i+1);
        

    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>>ans;
        vector<int>curr;
        help(ans,curr,nums,0);
        return ans;
    }
};
