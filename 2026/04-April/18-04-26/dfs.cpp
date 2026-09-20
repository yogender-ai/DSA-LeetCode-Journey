/*
 * DSA Lesson · Dfs
 *
 * Pattern : Data Structures & Algorithms
 * Written : 18 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
vector<bool> visited;
vector<int> result;

void  dfs(vector<vector<int>>a,int n){
        visited[n]=1;
        result.push_back(n);
        for(auto nn:a[n]){
            if(!visited[nn]){
                dfs(a,nn);
            }
        }
}
int main(){
    vector<vector<int>>adj(5);
    adj[0]={1,2};
    adj[1]={0,3};
    adj[2]={0,3};
    adj[3]={1,2,4};
    adj[4]={3};
    visited.assign(5, 0);
    dfs(adj,0);
    for(auto a:result){
        cout<<a<<' ';
    }

}
