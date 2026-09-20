/*
 * LeetCode 219 · Contains Duplicate II · Easy
 * https://leetcode.com/problems/contains-duplicate-ii/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int>mp;
        for(int i=0;i<nums.size();i++){
            if(mp.count(nums[i])) return true;
            mp.insert(nums[i]);
            if(mp.size()>k){
                mp.erase(nums[i-k]);
            }

        }
        return false;
    }
};
