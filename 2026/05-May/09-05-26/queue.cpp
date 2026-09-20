/*
 * DSA Lesson · Queue
 *
 * Pattern : Data Structures & Algorithms
 * Written : 09 May 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <queue>
#include<iostream>
using namespace std;
void pq(priority_queue<int>q,int a){
    for(int i=0;i<a;i++){
        int z;
        cin>>z;
        q.push(z);
    }
    cout<<"\n";
    cout<<q.top();
}
int main(){
     queue<int>q;
     q.push(2);
     q.push(3);
     q.push(4);
     q.push(5);
     q.push(6);
     while(!q.empty()){
        cout<<q.front();
        q.pop();
    }
    cout<<"This is priority queue\n";
    priority_queue<int>p;
    priority_queue<int,vector<int>,greater<int>>min;
    int a=5;
    pq(p,a);
    
}
