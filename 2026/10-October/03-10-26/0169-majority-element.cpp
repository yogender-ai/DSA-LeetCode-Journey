/*
 * LeetCode 169 · Majority Element · Easy
 * https://leetcode.com/problems/majority-element/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 3 Oct 2026
 * Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
 * Space   : O(1) · Memory: 42.2 MB (Beats 13.2%)
 */

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int>freq;
        for(auto &x:nums) freq[x]++;
        int max=0; int ans;
        for(auto &x: freq){
            if(x.second>max){
                max=x.second;
                ans=x.first;
            }
        }
        return ans;
    }
};
