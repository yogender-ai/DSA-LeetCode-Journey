/*
 * LeetCode 200 · Number of Islands · Medium
 * https://leetcode.com/problems/number-of-islands/
 *
 * Pattern : Graphs & Search
 * Solved  : 10 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int row=grid.size();
        int col=grid[0].size();

        vector<vector<int>>dirs={{-1,0},{1,0},{0,-1},{0,1}};
        int count=0;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){

                if(grid[i][j]=='1'){
                    count++;
                    queue<pair<int,int>>q;
                    q.push({i,j});

                    while(!q.empty()){
                        auto [r,c]=q.front();
                        q.pop();
                        for(auto d:dirs){
                            int qr=r+d[0];
                            int qc=c+d[1];
                            if(qr>=0&&qc>=0&&qr<row&&qc<col&&grid[qr][qc]=='1'){
                                q.push({qr,qc});
                                grid[qr][qc]=0;
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
};
