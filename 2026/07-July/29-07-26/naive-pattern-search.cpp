/*
 * DSA Lesson · Naive Pattern Search
 *
 * Pattern : Data Structures & Algorithms
 * Written : 29 Jul 2026
 * Time    : O(n * m)
 * Space   : O(1)
 */

#include<bits/stdc++.h>
using namespace std;
int main(){
  string a="ababcabc";
  string p="abc";
  int n=p.size();
  int q=a.size();
  for(int i=0;i<q;i++){
    string s=a.substr(i,n);

    if(s==p){
      cout<<i<<'\n';
    }

    if(i==(q-n)){
      break;
    }
  }
}
