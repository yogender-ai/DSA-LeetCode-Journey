/*
 * LeetCode 46 · Permutations · Medium
 * https://leetcode.com/problems/permutations/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 07 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    void help(vector<vector<int>>&ans,vector<int>&nums,vector<int>&curr,vector<bool>pick){
        if(curr.size()==nums.size()){
            ans.push_back(curr);
            return;
        }
        
        for(int i=0;i<nums.size();i++){
            if(pick[i]) continue;
            pick[i]=1;
            curr.push_back(nums[i]);
            help(ans,nums,curr,pick);
            curr.pop_back();
            pick[i]=0;
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>curr;
        vector<bool>pick(nums.size(),0);
        help(ans,nums,curr,pick);
        return ans;
    }
    
};
