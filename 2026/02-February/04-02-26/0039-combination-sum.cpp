/*
 * LeetCode 39 · Combination Sum · Medium
 * https://leetcode.com/problems/combination-sum/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 04 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    void help(vector<int>&c,int t,vector<int>&curr,int index,vector<vector<int>>&ans){
        
        if(t==0){
            ans.push_back(curr);
            return;
        }
        if(index==c.size()||t<0){
            return;
        }
        if(c[index]<=t){
            curr.push_back(c[index]);
            help(c,t-c[index],curr,index,ans);
            curr.pop_back();

        }
        help(c,t,curr,index+1,ans);

    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>ans;
        vector<int>curr;
        help(candidates,target,curr,0,ans);
        return ans;
    }
    
};
