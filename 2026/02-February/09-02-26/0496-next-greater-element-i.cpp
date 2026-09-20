/*
 * LeetCode 496 · Next Greater Element I · Easy
 * https://leetcode.com/problems/next-greater-element-i/
 *
 * Pattern : Stack
 * Solved  : 09 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int>a;
        stack<int>b;
        unordered_map<int,int>c;
        for(auto num:nums2){
            while(!b.empty()&&b.top()<num){
                c[b.top()]=num;
                b.pop();
            }
            b.push(num);
           
        }
        while(!b.empty()){
            c[b.top()]=-1;
            b.pop();
        }
        for(auto n:nums1){
            a.push_back(c[n]);
        }
        return a;
    }   
};
