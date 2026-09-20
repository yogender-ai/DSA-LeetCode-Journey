/*
 * LeetCode 162 · Find Peak Element · Medium
 * https://leetcode.com/problems/find-peak-element/
 *
 * Pattern : Binary Search
 * Solved  : 01 Feb 2026
 * Time    : O(n), Space: O(1)
 * Space   : O(1)
 */

// LeetCode 162 - Find Peak Element
// Solved on: 2026-02-01
// Topic: Array, Binary Search
// Approach: Linear Scan (User Provided)
// Time: O(n), Space: O(1)

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int max=nums[0];
        int ans=0;
        for(int i=0;i<nums.size();i++){
            if(max<nums[i]){
                max=nums[i];
                ans=i;
            }
        }
        return ans;
    }
};
