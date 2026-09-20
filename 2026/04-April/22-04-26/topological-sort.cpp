/*
 * DSA Lesson · Topological Sort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 22 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
#include<list>
#include<stack>
using namespace std;
class graph{
    int v;
    vector<list<int>>g;
public:
    graph(int v){
        this->v=v;
        g.resize(v);

    }
    void insert(int u,int v){
        g[u].push_back(v);
    }
    void dfs(int curr,vector<int>&vis,stack<int>&s){
        vis[curr]=1;
        for(auto a:g[curr]){
            if(!vis[a]){
                dfs(a,vis,s);
            }
        }
        s.push(curr);
    }
    void ts(){
        vector<int>vis(v,0);
        stack<int>s;
        for(int i=0;i<v;i++){
            dfs(i,vis,s);
        }
        while(s.size()>0){
            cout<<s.top()<<" ";
            s.pop();
        }
        cout<<endl;
    }
};
int main(){
    graph g(6);
    g.insert(5,0);
    g.insert(4,0);
    g.insert(5,2);
    g.insert(2,3);
    g.insert(3,1);
    g.insert(4,1);
    g.ts();
}
