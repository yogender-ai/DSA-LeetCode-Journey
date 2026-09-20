/*
 * LeetCode 1051 · Height Checker · Easy
 * https://leetcode.com/problems/height-checker/
 *
 * Pattern : Sorting & STL
 * Solved  : 13 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int>a;
        a=heights;
        sort(heights.begin(),heights.end());
        int count=0;
        for(int i=0;i<heights.size();i++){
            if(heights[i]!=a[i]){
                count++;
            }
        }
        return count;

    }
};
