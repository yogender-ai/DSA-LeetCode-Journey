/*
 * LeetCode 153 · Find Minimum in Rotated Sorted Array · Medium
 * https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 *
 * Pattern : Binary Search
 * Solved  : 01 Feb 2026
 * Time    : O(log n), Space: O(1)
 * Space   : O(1)
 */

// LeetCode 153 - Find Minimum in Rotated Sorted Array
// Solved on: 2026-02-01
// Topic: Binary Search, Array
// Approach: Binary Search (Modified)
// Time: O(log n), Space: O(1)

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left=0;
        int right=nums.size()-1;
        int ans;
        while(left<right){
            int mid=left+(right-left)/2;
            
            if(nums[mid]>nums[right]){
                left=mid+1;
            }
            else{
                right=mid;
            }
        }
        return nums[left];
        
    }
};
