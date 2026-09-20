/*
 * DSA Lesson · Insertionsort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 12 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
void insertionSort(vector<int>&a){
    for(int i=1;i<a.size();i++){
        int key=a[i];
        int j=i-1;
        while(j>=0&&a[j]>key){
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=key;
    }
}
int main(){
    vector<int>a={23,1,10,5,2};
    insertionSort(a);
    for(auto x:a){
        cout<<x<<' ';
    }
}
