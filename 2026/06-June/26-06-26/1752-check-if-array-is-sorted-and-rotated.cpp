/*
 * LeetCode 1752 · Check if Array Is Sorted and Rotated · Easy
 * https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<bits/stdc++.h>
using namespace std;
int main(){
    int arr[]={1,2,3,4,5};
    int sizesof = sizeof(arr);
    int sizesoff=sizeof(arr[0]);
    cout<<sizesof;
    cout<<sizesoff;
    int n=sizesof/sizesoff;
    int t=0;
    for(int i=0;i<n-1;i++){
        if(arr[i]<arr[i+1]){
            t=t+1;
        }
        else{
            t=t-1;
        }
    }
    if(t==n-1){
        cout<<t<<"True";
    }
    else{
        cout<<t<<"False";
    }
    
}
