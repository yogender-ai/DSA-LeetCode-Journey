/*
 * LeetCode 69 · Sqrt(x) · Easy
 * https://leetcode.com/problems/sqrtx/
 *
 * Pattern : Binary Search
 * Solved  : 01 Feb 2026
 * Time    : O(log x), Space: O(1)
 * Space   : O(1)
 */

// LeetCode 69 - Sqrt(x)
// Solved on: 2026-02-01
// Topic: Binary Search, Math
// Approach: Binary Search
// Time: O(log x), Space: O(1)

class Solution {
public:
    int mySqrt(int x) {
        int left=1;
        int right=x/2;
        int ans=0;
        if(x<2){
            return x;
        }
        while(left<=right){
            long long mid=left+(right-left)/2;
            if(mid*mid==x){
                return mid;
            }
            else if(mid*mid<x){
                ans=mid;
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        return ans;
    }
};
