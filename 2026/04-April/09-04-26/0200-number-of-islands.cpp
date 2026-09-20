/*
 * LeetCode 200 · Number of Islands · Medium
 * https://leetcode.com/problems/number-of-islands/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 09 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
#include<list>
#include<string>
#include<queue>
using namespace std;
int main(){
    int raw=4;
    int col=5;
    vector<vector<string>>matrix= {
            {"1", "1", "1", "1", "0"},
            {"1", "1", "0", "1", "0"},
            {"1", "1", "0", "0", "0"},
             {"0", "0", "1", "0", "1"}
    };
    /*int count=0;
    queue<int>q;
    q.push(0);
    vector<int>vis(4,0);
    vis[0]=1;
    while(!q.empty()){
        int u=q.front();
        q.pop();
        for(int i=0;i<raw;i++){
            if(matrix[u][i]=="1"&&vis[i]==0){
                q.push(i);
                vis[i]=1;
                cout<<'{'<<u<<','<<i<<'}'<<' ';
            }
        }
        cout<<endl;
    }*/
    vector<vector<int>>visit(4,vector<int>(col,0));
    int dirs[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
    int count=0;
    for(int i=0;i<raw;i++){
        for(int j=0;j<col;j++){
            if(matrix[i][j]=="1"&&visit[i][j]==0){

                visit[i][j]=1;
                count++;
                queue<pair<int,int>>q;
                q.push({i,j});
                while(!q.empty()){
                    auto [r,c]=q.front();
                    q.pop();
                    for(auto d:dirs){
                        int qr=r+d[0];
                        int qc=c+d[1];
                        if(qr>=0&&qr<raw&&qc>=0&&qc<col&&visit[qr][qc]==0&&matrix[qr][qc]=="1"){
                            q.push({qr,qc});
                            visit[qr][qc]=1;
                        }
                    }
                }
            }
        }
    }
    cout<<count;
}
