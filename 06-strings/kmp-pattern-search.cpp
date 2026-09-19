/*
 * KMP (Knuth–Morris–Pratt) pattern search
 * Builds the LPS / prefix-function array, then finds every match.
 * Written : 29 Jul 2026
 * Time    : O(n + m)
 */
#include<bits/stdc++.h>
using namespace std;
int main(){
  string a="aabaaa";
  int n=a.size();
  vector<int>p(n,0);
  int len=0;
  int i=1;
  while(i<n){
    if(a[len]==a[i]){
      len++;
      p[i]=len;
      i++;


    }
    else{
      if(len!=0){
        len=p[len-1];
      }
      else{
        p[i]=0;

        i++;
      }
    }
  }
  cout<<"\n";
  string t = "aabaaaaabaaa";
  int num=t.size();
  int j=0;
  int k=0;
  while(k<num){
    if(t[k]==a[j]){
      k++;
      j++;
      if (n == j) {
        cout << k - j << '\n';
        j = p[j - 1];

      }
    }
    else{
      if(j!=0){
        j=p[j-1];
      }
      else{
        k++;
      }
    }

  }
}
