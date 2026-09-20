/*
 * LeetCode 566 · Reshape the Matrix · Easy
 * https://leetcode.com/problems/reshape-the-matrix/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 03 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int row=mat.size();
        int col=mat[0].size();
        if(row*col!=r*c){
            return mat;
        }
        else{
            int a=0,b=0;
            vector<vector<int>>arr(r,vector<int>(c));
            for(int i=0;i<row;i++){

                for(int j=0;j<col;j++){

                    arr[a][b]=mat[i][j];
                    b++;
                    if(b>=c){
                        a++;
                        b=0;
                    }

                }

            }
            return arr;
        }
    }
};
