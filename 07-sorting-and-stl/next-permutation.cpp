/*
 * All permutations with next_permutation()
 * Sort first, then loop until next_permutation returns false.
 * Written : 29 Jul 2026
 * Time    : O(n! * n)
 */
#include<bits/stdc++.h>
using namespace std;
int main(){
  string s="bac";
  sort(s.begin(),s.end());
  do{
    cout<<s<<'\n';
  }
  while(next_permutation(s.begin(),s.end()));
}
