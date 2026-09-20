/*
 * DSA Lesson · Bubblesort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 12 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
void bubbleSort(vector<int>&a){

    for(int i=0;i<a.size()-1;i++){
        for(int j=0;j<a.size()-i-1;j++){
            if(a[j]>a[j+1]){
                swap(a[j],a[j+1]);
            }
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int>a={5,1,4,2,8};
    bubbleSort(a);
    for(auto x:a){
        cout<<x<<' ';
    }
}
