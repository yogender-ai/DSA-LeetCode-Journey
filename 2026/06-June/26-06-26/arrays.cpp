/*
 * DSA Lesson · Arrays
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

//Linear search 
#include<iostream>
#include<array>
using namespace std;
int main() {
    array<int,5>arr={1,2,3,4,5};
    int target=2;
    for(int i=0;i<size(arr);i++){
        if(arr[i]==target){
            cout<<i;
            break;
        }
    }
}
