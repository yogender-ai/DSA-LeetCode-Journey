/*
 * LeetCode 278 · First Bad Version · Easy
 * https://leetcode.com/problems/first-bad-version/
 *
 * Pattern : Binary Search
 * Solved  : 01 Feb 2026
 * Time    : O(log n), Space: O(1)
 * Space   : O(1)
 */

// LeetCode 278 - First Bad Version
// Solved on: 2026-02-01
// Topic: Binary Search
// Approach: Binary Search (Minimize comparison)
// Time: O(log n), Space: O(1)

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left=0;
        int right=n;
        while(left<right){
            int mid=left+(right-left)/2;
            if(isBadVersion(mid)==0){
                left=mid+1;
            }
            else{
                right=mid;
            }
        }
        return left;
    }
};
