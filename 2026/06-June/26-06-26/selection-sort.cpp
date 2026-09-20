/*
 * DSA Lesson · Selection Sort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
int main(){
    int size;
    cout<<"Size of the Array:- ";
    cin>>size;
    cout<<'\n';
    int arr[size];
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }

    for(int i=0;i<size;i++){
        int min=arr[i];
        int temp=arr[i];
        for(int j=i+1;j<size;j++){
            if(min>arr[j]){
                min=j;

            }
        }
        arr[i]=arr[min];
        arr[min]=temp;
        cout<<arr[i]<<' ';
    }
    return 0;
}
