/*
 * DSA Lesson · Graph List
 *
 * Pattern : Data Structures & Algorithms
 * Written : 07 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
#include<list>
using namespace std;
int main(){
    int vertex =4;
    int e=4;
    vector<vector<int>>l(4);
    vector<pair<int,int>>edges={{0,1},{0,2},{2,3},{1,2}};
    for(auto edge:edges){
        int u=edge.first;
        int v=edge.second;
        l[u].push_back(v);
        l[v].push_back(u);

    }
    for(int i=0;i<vertex;i++){
        for(auto x:l[i]){
            cout<<x<<' ';
        }
        cout<<'\n';
    }

}
