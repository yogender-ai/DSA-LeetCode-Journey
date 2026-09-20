/*
 * LeetCode 3834 · Merge Adjacent Equal Elements · Medium
 * https://leetcode.com/problems/merge-adjacent-equal-elements/
 *
 * Pattern : Stack
 * Solved  : 08 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<long long> mergeAdjacent(vector<int>& nums) {
        vector<long long>ans;
        int n=nums.size();
        int i=0;
        for(auto x:nums){
            long long cur=x;
            while(!ans.empty()&&ans.back()==cur){
                cur+=ans.back();
                ans.pop_back();
            }
            ans.push_back(cur);
            
        }
        return ans;
    }
};
