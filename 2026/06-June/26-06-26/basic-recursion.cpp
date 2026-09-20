/*
 * DSA Lesson · Basic Recursion
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

/*#include <bits/stdc++.h>
using namespace std;
int main(){
int d=0;
string a="Aba";
int b=a.size();
for(int i=0,k=1;i<b;i++,k++){
  if(a[i]==a[b-k])
  { 
    d++;
  }
  else {
    d--;
  }
}
if(d==b){
  cout<<"It is palindrom";

}
else {
  cout<<"it is not";
}
}*/
/*#include <bits/stdc++.h>
using namespace std;
int main() {
  int a;
  cin>>a;
  int sum=0;
  while (a>0) {
    int q=a%10;

    sum=q+sum;
    a=a/10;
  }
  cout<<sum;

}*/
#include<iostream>
using namespace std;
void print(int n) {
    if (n==0) return;
    print(n-1);
    cout<<n<<" "<<flush;
}
int main() {
    int a=4;
    cout<<endl;
    print(a);

}
