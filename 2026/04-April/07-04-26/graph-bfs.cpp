/*
 * DSA Lesson · Graph Bfs
 *
 * Pattern : Data Structures & Algorithms
 * Written : 07 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<list>
#include<vector>
#include<queue>
using namespace std;
class Graph{
    int v;
    vector<vector<int>>graph;
public:
    Graph(int v){
        this->v=v;
        graph.resize(v);
    }
    void insert(int u,int v){
        graph[u].push_back(v);
        graph[v].push_back(u);

    }
    void bfs(int b){
        vector<int>vis(v,0);
        queue<int>q;
        q.push(b);
        vis[b]=1;
        cout<<b<<' ';
        while(!q.empty()){
            int u=q.front();
            q.pop();

            for(auto x:graph[u]){
                if(vis[x]!=1){
                    q.push(x);
                    vis[x]=1;
                    cout<<x<<" ";
                }

            }

        }
    }
};
int main(){
    Graph obj(4);
    obj.insert(0,1);
    obj.insert(0,2);
    obj.insert(2,3);
    obj.insert(1,2);
    obj.bfs(0);
}
