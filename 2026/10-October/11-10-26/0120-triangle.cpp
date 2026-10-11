/*
 * LeetCode 120 · Triangle · Medium
 * https://leetcode.com/problems/triangle/
 *
 * Pattern : Dynamic Programming
 * Solved  : 11 Oct 2026
 * Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
 * Space   : O(1) · Memory: 12.6 MB (Beats 91.4%)
 */

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        
        for(int i = n - 2; i >= 0; i--) {
            for(int j = 0; j < triangle[i].size(); j++) {
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]);
            }
        }
        
        return triangle[0][0];
    }
};
