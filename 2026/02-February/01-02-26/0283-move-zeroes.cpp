/*
 * LeetCode 283 · Move Zeroes · Easy
 * https://leetcode.com/problems/move-zeroes/
 *
 * Pattern : Two Pointers
 * Solved  : 01 Feb 2026
 * Time    : O(n), Space: O(n)
 * Space   : O(n)
 */

// LeetCode 283 - Move Zeroes
// Solved on: 2026-02-01
// Topic: Array, Two Pointers
// Approach: Auxiliary Array (Brute Force)
// Time: O(n), Space: O(n)

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int>a;
        int count=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=0){
                a.push_back(nums[i]);
            }
            else{
                count++;
            }   
        }
        for(int i=0;i<count;i++){
            a.push_back(0);
        }
        for(int i=0;i<a.size();i++){
            nums[i]=a[i];
        }

    }
};
