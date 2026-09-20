/*
 * DSA Lesson · String Basics
 *
 * Pattern : Data Structures & Algorithms
 * Written : 29 Jul 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<bits/stdc++.h>
using namespace std;
int main(){
  string s;
  cout<<"Write your name\n";
  getline(cin,s);
  cout<<s<<'\n';
  //cout<<"All capital letters "<<toupper(s)<<'\n';  --toupper() is used for only char
  //out<<"All small letters "<<tolower(s)<<'\n';     --tolower() is used for only char
  try {
    int num=stoi(s);
    cout<<"string to numbers"<<num<<'\n';
  }
  catch(...){
    cout<<"Not a number\n";
  }
  cout<<"String length "<<s.size()<<'\n';
  reverse(s.begin(), s.end());
  cout << "String reverse " << s << '\n';
  reverse(s.begin(), s.end());
  vector<int> freq(26, 0);
  for(auto x:s){
    freq[x-'a']++;
  }
  cout<<"Frequency of the string=>\n";
  for(size_t i=0;i<s.size();i++){
    cout<<s[i]<<' '<<freq[s[i]-'a']<<'\n';
  }
  cout<<s.front()<<' '<<s.back();
  s.push_back('!');
  cout<<s<<'\n';
  s.pop_back();
  cout<<s<<'\n';
  string a;
  getline(cin,a);
  stringstream q(a);
  int z;
  string x;
  double c;
  q>>z>>x>>c;
  cout<<x<<' '<<z<<' '<<c<<'\n'; 

}
