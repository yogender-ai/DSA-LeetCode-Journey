/*
 * LeetCode 344 · Reverse String · Easy
 * https://leetcode.com/problems/reverse-string/
 *
 * Pattern : Two Pointers
 * Solved  : 03 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    void rr(vector<char>&c,int l,int r){
        if(l>=r) return;
        swap(c[l],c[r]);
        rr(c, l+1,r-1);
    }
    void reverseString(vector<char>& s) {
        rr(s,0,s.size()-1);

    }
};
