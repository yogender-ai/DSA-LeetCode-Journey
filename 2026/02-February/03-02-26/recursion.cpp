/*
 * DSA Lesson · Recursion
 *
 * Pattern : Data Structures & Algorithms
 * Written : 03 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
using namespace std;
int  sum(int n){
    if(n<1){
        return n;
    }
    return n+sum(n-1);
}
int main(){
    int a=3;
    cout<<sum(3);
    /*int j=0;
    for(int i=0;i<=a;i++){
        j+=i;
    }
    cout<<j;*/

}
