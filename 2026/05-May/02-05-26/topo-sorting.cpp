/*
 * DSA Lesson · Topo Sorting
 *
 * Pattern : Data Structures & Algorithms
 * Written : 02 May 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
class graph{
    vector<vector<int>>list;
public:
    graph(int a){
        list.resize(a);
    }
    void insert(int a,int b){
        list[a].push_back(b);
    }
    void dfs(int a,vector<int>&vis){
        vis[a]=1;
        cout<<a<<" ";
        for(auto v:list[a]){
            if(vis[v]==0){
                dfs(v,vis);
            }
        }
    }
    void dfs(int a){
        vector<int>vis(list.size(),0);
        dfs(a,vis);
    }
    void topo(int a,vector<int>&vis,vector<int>&order){
        vis[a]=1;
        for(auto v:list[a]){
            if(vis[v]==0){
                topo(v,vis,order);
            }
        }
        order.push_back(a);
    }
    void topo(int a){
        vector<int>vis(list.size(),0);
        vector<int>order;
        topo(a,vis,order);
        reverse(order.begin(),order.end());
        for(auto a:order){
            cout<<a<<" ";
        }
    }
};

int main(){
    graph obj(5);
    obj.insert(1,2);
    obj.insert(2,3);
    obj.insert(3,4);

    obj.dfs(1);
    cout<<endl;
    obj.topo(1);

}
