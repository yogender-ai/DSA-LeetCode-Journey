/*
 * LeetCode 40 · Combination Sum II · Medium
 * https://leetcode.com/problems/combination-sum-ii/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 04 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    void help(vector<int>&c,int t,vector<vector<int>>&ans,vector<int>&curr,int i){
        if(t==0){
            ans.push_back(curr);
            return;
        }
        if(i==c.size()||t<0){
            return;
        }
        if(c[i]<=t){
            curr.push_back(c[i]);
            help(c,t-c[i],ans,curr,i+1);
            curr.pop_back();
        }
        while (i + 1 < c.size() && c[i] == c[i + 1])
            i++;

        
        help(c, t, ans, curr, i + 1);
        
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<vector<int>>ans;
        vector<int>curr;
        help(candidates,target,ans,curr,0);
        return ans;
    }
};
