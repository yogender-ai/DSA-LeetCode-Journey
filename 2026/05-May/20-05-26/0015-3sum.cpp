/*
 * LeetCode 15 · 3Sum · Medium
 * https://leetcode.com/problems/3sum/
 *
 * Pattern : Two Pointers
 * Solved  : 20 May 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int r=nums.size()-1;
        int l=0;
        set<vector<int>>st;
        vector<vector<int>>ans;
        sort(nums.begin(),nums.end());

        for(int i=0;i<nums.size();i++){
            int l=i+1;
            int r=nums.size()-1;
            while(l<r){
                int sum=nums[i]+nums[l]+nums[r];
                if(sum==0){
                    st.insert({nums[i],nums[l],nums[r]});
                    l++;
                    r--;
                }
                else if(sum<0){
                    l++;
                }
                else{
                    r--;
                }
            }
        }
        for(auto x : st){
            ans.push_back(x);
        }
        return ans;
    }
};
