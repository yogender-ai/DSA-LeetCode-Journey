/*
 * LeetCode 349 · Intersection of Two Arrays · Easy
 * https://leetcode.com/problems/intersection-of-two-arrays/
 *
 * Pattern : Two Pointers
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int>q(nums1.begin(),nums1.end());
        unordered_set<int>w(nums2.begin(),nums2.end());
        vector<int>a;
        for(auto x:q){
            if(w.count(x)){
                a.push_back(x);
            }
        }
        return a;
    }
};
