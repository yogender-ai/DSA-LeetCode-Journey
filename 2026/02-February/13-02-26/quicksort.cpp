/*
 * DSA Lesson · Quicksort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 13 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
int partition(vector<int>&a,int st,int end){
    int idx=st-1,pi=a[end];
    for(int i=st;i<end;i++){
        if(pi>=a[i]){
            idx++;
            swap(a[idx],a[i]);
        }
    }
    idx++;
    swap(a[idx],a[end]);
    return idx;
}
void quick(vector<int>&a,int l,int r){
    if(l<r){
        int pivot= partition(a,l,r);
        quick(a,l,pivot-1);
        quick(a,pivot+1,r);
    }
}
int main(){
    vector<int>a={3,2,3,1,2,4,5,5,6};
    int right=a.size()-1;
    quick(a,0,right);
    for(auto x:a){
        cout<<x<<" ";
    }
}
