/*
 * DSA Lesson · Dijkstra
 *
 * Pattern : Data Structures & Algorithms
 * Written : 18 May 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
#include<queue>
#include <climits>
#include <functional> 
using namespace std;
void dij(int src,int n , vector<vector<pair<int,int>>>adj){
    vector<int>dist(n,INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater <>>pq;
    pq.push({0,src});
    dist[src]=0;
    while(!pq.empty()){
        auto [d,q]=pq.top();
        pq.pop();
        if(d>dist[q]) continue;
        for(auto [v,w]: adj[q]){
            if(dist[q]+w<dist[v]){
                dist[v]=w+dist[q];
                pq.push({dist[v],v});

            }
        }
    }
    for(auto x:dist){
        cout<<x<<' ';
    }
}
int main(){
    vector<vector<pair<int,int>>>adj(4);
    adj[0]={{1,4},{2,2}};
    adj[1]={{3,3}};
    adj[2]={{3,3},{1,1}};
    adj[3]={};
    dij(0,4,adj);
}
