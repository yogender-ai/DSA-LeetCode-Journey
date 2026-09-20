/*
 * LeetCode 704 · Binary Search · Easy
 * https://leetcode.com/problems/binary-search/
 *
 * Pattern : Binary Search
 * Solved  : 01 Feb 2026
 * Time    : O(log n), Space: O(1)
 * Space   : O(1)
 */

// LeetCode 704 - Binary Search
// Solved on: 2026-02-01
// Topic: Binary Search
// Approach: Iterative/Recursive (User Provided)
// Time: O(log n), Space: O(1)

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size()-1;
        int ans=-1;
        while(left<=right){
            int mid=(left+right)/2;
            if(nums[mid]==target){
                ans=mid;
            }
            if(nums[mid]>target){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        return ans;

    }
};
