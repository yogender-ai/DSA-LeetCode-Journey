/*
 * LeetCode 78 · Subsets · Medium
 * https://leetcode.com/problems/subsets/
 *
 * Pattern : Bit Manipulation
 * Solved  : 06 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    void help(vector<int>&n,vector<vector<int>>&ans,int i,vector<int>&curr){
        if(i==n.size()){
            ans.push_back(curr);
            return ;
        }
        
        curr.push_back(n[i]);
        help(n,ans,i+1,curr);
        curr.pop_back();
        help(n,ans,i+1,curr);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>curr;
        
        help(nums,ans,0,curr);
        return ans;
    }
};
