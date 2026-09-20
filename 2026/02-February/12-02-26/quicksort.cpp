/*
 * DSA Lesson · Quicksort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 12 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
int partition(vector<int>&a,int st,int end){
    int idx=st-1,pivot=a[end];
    for(int j=st;j<end;j++){
        if(a[j]<=pivot){
            idx++;
            swap(a[idx],a[j]);
        }
    }
    idx++;
    swap(a[idx],a[end]);
    return idx;

}
void quick(vector<int>&a,int l,int r){
    if(l<r){
    int  pi=partition(a,    l,r);
    quick(a,l,pi-1);
    quick(a,pi+1,r);

    }

}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int>a={5,2,6,4,1,3};
    int pi=a[a.size()-1];
    quick(a,0,a.size()-1);
    for(auto x:a){
        cout<<x<<' ';
    }
}
