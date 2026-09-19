/*
 * sort() vs stable_sort()
 * Same output for ints; stable_sort keeps equal keys in original order.
 * Written : 29 Jul 2026
 * Time    : O(n log n)
 */
#include<bits/stdc++.h>
using namespace std;
int main(){
  vector<int>a={5,1,5,1,5,1,2,2,2};
  vector<int>b=a;
  sort(a.begin(),a.end());
  stable_sort(b.begin(),b.end());
  for(int x:a){
    cout<<x<<' ';
  }
  cout<<'\n';
  for (int x : b) {
    cout << x << ' ';
  }
}
