/*
 * LeetCode 217 · Contains Duplicate · Easy
 * https://leetcode.com/problems/contains-duplicate/
 *
 * Pattern : Hash Set
 * Solved  : 24 Dec 2025
 * Time    : O(n)
 * Space   : O(n)
 */

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> st; // Unordered Set
        for(auto &x :nums){
            if(st.count(x)) { // Duplicate Found
                return true ;
            }
            st.insert(x); // Duplicate Not Found! Inserting in Set
        }
        return false;
    }
};
