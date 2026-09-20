/*
 * DSA Lesson · Dfs
 *
 * Pattern : Data Structures & Algorithms
 * Written : 24 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
#include <list>
#include<queue>
using namespace std;
class graph{
    int n;
    vector<list<int>>g;
public:
    graph(int n){
        this->n=n;
        g.resize(n);
    }
    void insert(int u,int v ){
        g[u].push_back(v);
        g[v].push_back(u); //undirected graph
    }
    void bfs(int choice){
        queue<int>q;
        vector<int>vis(n,0);
        q.push(choice);
        vis[choice]=1;
        while(!q.empty()){
            int u=q.front();
            q.pop();
            cout<<u<<" ";
            for(int x:g[u]){
                if(!vis[x]){
                    q.push(x);
                    vis[x]=1;
                }
            }
        }
    }
    void dfs(int source,vector<int>&vis){
        cout<<source<<' ';
        vis[source]=1;
        for(int x:g[source]){
            if(!vis[x]){
                dfs(x,vis);
            }
        }
    }
    void dfs(int source){
        vector<int>vis(n,0);
        dfs(source,vis);
    }
};
int main(){
    graph g(5);
    g.insert(0,1);
    g.insert(1,2);
    g.insert(2,4);
    g.insert(1,3);
    g.bfs(0);
    cout<<endl;
    g.dfs(0);
}
