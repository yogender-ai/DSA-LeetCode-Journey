#include<bits/stdc++.h>
using namespace std;
int main(){
  /*string s="hello";
  int count=0;

  for(char x:s){

    count+=x;
  }
  cout<<count;*/
  vector<int>q={2,0,20,0,1,1,0};
  /*sort(q.begin(),q.end(),greater <int>());
  for(int x:q){
    cout<<x<<' ';
  }*/
  vector<int>w;
  vector<int>e;
  for(int x:q){
    if(x!=0){
      w.push_back(x);
    }
  }
  for(int x:q){
    if(x==0){
      e.push_back(x);
    }
  }
  w.insert(w.end(),e.begin()+1,e.end());
  for(int x:w){
    cout<<x<<' ';
  }

  
}
