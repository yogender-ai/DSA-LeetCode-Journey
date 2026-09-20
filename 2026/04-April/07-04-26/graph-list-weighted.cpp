/*
 * DSA Lesson · Graph List Weighted
 *
 * Pattern : Data Structures & Algorithms
 * Written : 07 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<list>
#include<vector>
using namespace std;
int main(){
    int v=4;

    vector<vector<pair<int,int>>>li(v);
    for(int i=0;i<v;i++){
        int q,w,e;
        cin>>q>>e>>w;
        li[q].push_back({e,w});
        li[e].push_back({q,w});
    }
    for(int i=0;i<v;i++){
        for(auto [r,t]:li[i]){
            cout<<i<<"->"<<r<<"||"<<t<<'\n';
        }
        cout<<'\n';
    }
}
