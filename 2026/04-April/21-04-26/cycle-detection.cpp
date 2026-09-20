/*
 * DSA Lesson · Cycle Detection
 *
 * Pattern : Data Structures & Algorithms
 * Written : 21 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;

vector<int>visit;

bool cycle_d(vector<vector<int>>adj,int a,int par){
visit[a]=1;
for(auto d:adj[a]){
    if(!visit[d]){
        if(cycle_d(adj,d,a)){
            return 1;
        }

    }
    else if(d!=par){
        return 1;
    }

}
return 0;


}
int main(){
    vector<vector<int>>adj(4);
    adj[0]={1,2};
    adj[1]={0,3};
    adj[2]={3,0};
    adj[3]={2,1};
    visit.resize(4,-1);

    cycle_d(adj,0,-1);
    if(cycle_d){
        cout<<"yes";
    }
    else{
        cout<<"NO";
    }


}
