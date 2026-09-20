/*
 * LeetCode 47 · Permutations II · Medium
 * https://leetcode.com/problems/permutations-ii/
 *
 * Pattern : Sorting & STL
 * Solved  : 07 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    void help(vector<vector<int>>&ans,vector<int>&curr,vector<int>&used,vector<int>&nums){
        if(curr.size()==nums.size()){
            ans.push_back(curr);
            return;
        }
        for(int i=0;i<nums.size();i++){
            if(used[i])continue;
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])
                continue;
            curr.push_back(nums[i]);
            used[i]=1;
            help(ans,curr,used,nums);
            curr.pop_back();
            used[i]=0;
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>curr;
        vector<int>used(nums.size(),0);
        sort(nums.begin(),nums.end());
        help(ans,curr,used,nums);
        return ans;
    }
};
