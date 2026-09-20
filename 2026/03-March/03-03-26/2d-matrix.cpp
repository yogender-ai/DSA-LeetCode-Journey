/*
 * DSA Lesson · 2D Matrix
 *
 * Pattern : Data Structures & Algorithms
 * Written : 03 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
int main(){
    int r=3;
    int c=4;
    int arr[3][4];

    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cin>>arr[i][j];
        }
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<"\n";
    }

}
