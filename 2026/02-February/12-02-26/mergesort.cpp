/*
 * DSA Lesson · Mergesort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 12 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
void merge(vector<int>&a,int left,int mid,int right){

    int n1=mid-left+1;
    int n2=right-mid;
    vector<int>q1(n1);
    vector<int>q2(n2);
    for(int i=0;i<mid-left+1;i++){
        q1[i]=a[left+i];
    }
    for(int i=0;i<right-mid;i++){
        q2[i]=a[mid+1+i];
    }
    int i=0;
    int j=0;
    int k=left;
    while(i<n1&&j<n2){
        if(q1[i]<=q2[j]){
           a[k]=q1[i];
           i++;
           k++;
        }
        else {
            a[k]=q2[j];
            j++;
            k++;

        }
    }
    while(i<n1){
        a[k]=q1[i];
        k++;
        i++;
    }
    while(j<n2){
        a[k]=q2[j];
        k++;
        j++;
    }


}
void mergeSort(vector<int>&a,int left,int right){

    if(left >= right) return;
    int mid=left+(right-left)/2;

    mergeSort(a,left,mid);
    mergeSort(a,mid+1,right);
    merge(a,left,mid,right);
}
int main(){
    vector<int>a={3,8,2,5,7,15,10,18};
    mergeSort(a,0,a.size()-1);
    for(auto x:a){
        cout<<x<<' ';
    }
}
