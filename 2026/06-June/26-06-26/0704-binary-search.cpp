/*
 * LeetCode 704 · Binary Search · Easy
 * https://leetcode.com/problems/binary-search/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
int b_s(int arr[],int s,int number){
    int left=0;
    int right=s-1;

    cout<<s<<'\n';
    int mid=s/2;
    for(int i=0;i<=s;i++){

        if(number==arr[mid]){
            break;
        }
        else if(number>arr[mid]){
            left=mid+1;
            right=s;
            mid=(left+right)/2;
        }
        else{
            left=0;
            right=mid-1;
            mid=(left+right)/2;
        }

    }
    return mid;


};
int main(){
    int size;
    cout<<"Write the size of an Array:- ";
    cin>>size;
    cout<<'\n';
    int ar[size];
    for(int i=0;i<size;i++){
        cin>>ar[i];
    }
    cout<<'\n'<<"No. to find:- ";
    int a;
    cin>>a;
    cout<<b_s(ar,size,a);

}
