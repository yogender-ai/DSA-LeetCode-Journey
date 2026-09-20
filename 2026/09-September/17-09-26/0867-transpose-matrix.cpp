/*
 * LeetCode 867 · Transpose Matrix · Easy
 * https://leetcode.com/problems/transpose-matrix/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 03 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int r=matrix.size();
        int c=matrix[0].size();
        if(r==c){

            for(int i=0;i<r;i++){
                for(int j=0;j<=i&&j<c;j++){
                    if(i!=j){
                        swap(matrix[i][j],matrix[j][i]);
                    }
                }
            }
            return matrix;
        }
        else{
            vector<vector<int>>arr(c,vector<int>(r));
            for(int i=0;i<c;i++){
                for(int j=0;j<r;j++){
                    arr[i][j]=matrix[j][i];
                }
            }
            return arr;
        }
    }
};
