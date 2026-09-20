/*
 * DSA Lesson · Bitmanipulation
 *
 * Pattern : Data Structures & Algorithms
 * Written : 17 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
int set(int a,int b){
    return a|=(1<<b);
}
int unset(int a,int b){
    return a&=(~(1<<b));
}
int toggle(int a,int b){
    return a^=(1<<b); //a^a==0
}
bool checkset(int a,int b){
    //0100&0100 if it gives
    int bit= a&(1<<b);
}
int main(){
    int a,b; //4= 0100
    cin>>a>>b;
    cout<<set(a,b)<<'\n';
    cout<<unset(a,b)<<'\n';
    cout<<toggle(a,b)<<'\n';
}
