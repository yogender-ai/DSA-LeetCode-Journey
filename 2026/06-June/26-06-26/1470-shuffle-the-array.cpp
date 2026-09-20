/*
 * LeetCode 1470 · Shuffle the Array · Easy
 * https://leetcode.com/problems/shuffle-the-array/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int>q;
        for(int i=0;i<n;i++){
            q.push_back(nums[i]);
            q.push_back(nums[i+n]);
        }
        return q;
    }
};
