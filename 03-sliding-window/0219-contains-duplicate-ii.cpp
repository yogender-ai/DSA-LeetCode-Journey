/*
 * LeetCode 219 · Contains Duplicate II · Easy
 * https://leetcode.com/problems/contains-duplicate-ii/
 *
 * Pattern : Fixed-size Sliding Window + Hash Set
 * Solved  : 28 Dec 2025
 * Time    : O(n)
 * Space   : O(k)
 */
#include <bits/stdc++.h>
using namespace std;

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
