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


