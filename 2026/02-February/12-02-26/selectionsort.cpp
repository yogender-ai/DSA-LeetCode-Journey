/*
 * DSA Lesson · Selectionsort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 12 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
using namespace std;
void sort(vector<int>&q){
    int min=0;
    for(int i=0;i<q.size();i++){
        min=q[i];
        int temp=i;
        for(int j=i+1;j<q.size();j++){
            if(min>q[j]){
                min=q[j];
                temp=j;
            }
        }
        q[temp]=q[i];
        q[i]=min;
    }
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int>a={45,34,11,65,35,9,1,32};
    sort(a);
    for(auto x:a){
        cout<<x<<' ';
    }
}
