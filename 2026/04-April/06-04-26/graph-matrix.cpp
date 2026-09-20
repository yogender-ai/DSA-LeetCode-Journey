/*
 * DSA Lesson · Graph Matrix
 *
 * Pattern : Data Structures & Algorithms
 * Written : 06 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
#include<utility>
using namespace std;
int main(){
    int v=4;
    vector<vector<int>>matrix(v,vector<int>(v,0));
    int e=4;
    vector<pair<int,int>>edges={{0,1},{0,2},{1,2},{2,3}};
    for(auto edge:edges){
        int u=edge.first;
        int v=edge.second;
        matrix[u][v]=1;
        matrix[v][u]=1;
    }
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            cout<<matrix[i][j]<<' ';
        }
        cout<<'\n';
    }
}
