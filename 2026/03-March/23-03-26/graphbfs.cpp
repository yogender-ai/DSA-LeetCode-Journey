/*
 * DSA Lesson · Graphbfs
 *
 * Pattern : Data Structures & Algorithms
 * Written : 23 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

//
// Created by yashk on 23-03-2026.
//
#include<iostream>
#include<list>
#include<vector>
#include <queue>
using namespace std;
class graph{
    vector<list<int>>l;
    int v;
public:

    graph(int v){  //constructor always public so that we can create object
        this->v=v;
        l.resize(v);
    }

    void insert(int u,int q){
        l[u].push_back(q);
        l[q].push_back(u);
    }
    void bfs(){ //O(vertices + edges)
        queue<int>q;
        vector<int>vis(v,0);
        q.push(0);
        vis[0]=1;
        while(!q.empty()){
            int u=q.front();
            q.pop();
            cout<<u<<" ";
            for(int x:l[u]){
                if(!vis[x]){
                    vis[x]=1;
                    q.push(x);
                }
            }
        }

    }
};
int main(){
    graph g(5);
    g.insert(0,1);
    g.insert(1,2);
    g.insert(1,3);
    g.insert(2,3);
    g.insert(2,4);
    g.bfs();

}
