/*
 * DSA Lesson · Recursion Revision
 *
 * Pattern : Data Structures & Algorithms
 * Written : 08 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
void help(vector<int>&a,vector<vector<int>>&q,vector<int>&curr,vector<int>&used){
    if(curr.size()==a.size()){
        q.push_back(curr);
        return;
    }

    for(int i=0;i<a.size();i++){
        if(used[i]==1){
            continue;
        }
        used[i]=1;
        curr.push_back(a[i]);
        help(a,q,curr,used);
        curr.pop_back();
        used[i]=0;
    }

}
vector<vector<int>>ans(vector<int>&a){
    vector<int>curr;
    vector<vector<int>>q;
    vector<int>used={0,3};
    help(a,q,curr,used);
    return q;
}
int main(){
    vector<int>a={1,2,3};
    vector<vector<int>>res=ans(a);
    for(auto r:res){
        for(auto col:r){
            cout<<col<<' ';
        }
        cout<<'\n';
    }
}
