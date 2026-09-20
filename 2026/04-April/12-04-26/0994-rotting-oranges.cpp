/*
 * LeetCode 994 · Rotting Oranges · Medium
 * https://leetcode.com/problems/rotting-oranges/
 *
 * Pattern : Graphs & Search
 * Solved  : 12 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int row=grid.size();
        int col=grid[0].size();
        int fresh=0;
        queue<pair<int,int>>q;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if(grid[i][j]==2){
                    q.push({i,j});
                }
                else if (grid[i][j]==1){
                    fresh++;
                }
            }
        }
        int min=0;
        vector<vector<int>>dirs={{-1,0},{1,0},{0,-1},{0,1}};
        while(!q.empty() && fresh>0){

            int sz=q.size();

            min++;
            for(int i=0;i<sz;i++){
                auto [r,c]=q.front();
                q.pop();
                for(auto d:dirs){
                    int qr=r+d[0];
                    int qc=d[1]+c;
                    if(qr >= 0 && qr < row && qc >= 0 && qc < col&&grid[qr][qc]==1){
                        q.push({qr,qc});
                        grid[qr][qc]=2;
                        fresh--;
                    }

                }
            }


        }
        return fresh==0?min:-1;
    }
};

