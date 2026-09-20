/*
 * DSA Lesson · Array Searching
 *
 * Pattern : Data Structures & Algorithms
 * Written : 23 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

//wrong 
/*
#include<iostream>
using namespace std;
int main(){
    int arr[5]={1,2,3,4,5};
    //linear searching 
    
    int target=2;
    for(int i=0;i<arr.size();i++){
        if(target=arr[i]){
            cout<<i;
            break;
        }
        else{
            cout<<"None";
        }
    }
}*/

//c++17+
/*
#include<iostream>
#include<iterator>
using namespace std;
int main(){
    int arr[5]={1,2,3,4,5};
    //linear searching 
    
    int target=2;
    for(int i=0;i<size(arr);i++){
        if(target=arr[i]){
            cout<<i;
            break;
        }
        else{
            cout<<"None";
        }
    }
}
    */

#include<iostream>
#include<array>
using namespace std;
int main(){
    array<int,5>arr={1,2,3,4,5};
    //linear searching 
    
    int target=2;
    for(int i=0;i<arr.size();i++){
        if(target=arr[i]){
            cout<<i;
            break;
        }
        else{
            cout<<"None";
        }
    }
}
