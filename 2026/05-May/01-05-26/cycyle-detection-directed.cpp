/*
 * DSA Lesson · Cycyle Detection Directed
 *
 * Pattern : Data Structures & Algorithms
 * Written : 01 May 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
class graph{
    vector<vector<int>>list;
public:
    graph(int a){  //This is the public constructor we are making it public to create object in main function
        list.resize(a+2);

    }
    void insert(int q,int w){
        list[q].push_back(w);

    }
    void dfs(int a, vector<int>&vis){
        vis[a]=1;
        cout<<a<<' ';
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
    bool cdetect(int a,vector<int>&vis,vector<int>&path){
         vis[a]=1;
         path[a]=1;
         for(int v:list[a]){
             if(path[v]==1){
                 return 1;
             }
             if(vis[v]==0){
                 if(cdetect(v,vis,path)){
                     return 1;
                 }
             }
         }
         path[a]=0;
         return 0;
    }
    bool cdetect(int a){
        vector<int>vis(list.size());
        vector<int>path(list.size());
        return cdetect(a,vis,path);

    }

};
int main(){
    // 1->2->4->5->3
    graph obj(5);
    obj.insert(1,2);
    obj.insert(2,4);
    obj.insert(4,5);
    obj.insert(5,3);
    obj.insert(3,4);
    obj.dfs(1);
    cout<<endl;

    cout<<obj.cdetect(1);



}
