/*
 * LeetCode 31 · Next Permutation · Medium
 * https://leetcode.com/problems/next-permutation/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 29 Jul 2026
 * Time    : O(n)
 * Space   : O(1)
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
