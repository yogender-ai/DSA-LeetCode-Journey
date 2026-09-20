/*
 * DSA Lesson · Strings
 *
 * Pattern : Data Structures & Algorithms
 * Written : 30 Jan 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include<string>
using namespace std;
int main(){
    string a="abcd";
    cout<<a.size()<<'\n';
    string b="Hello";
    string sub=b.substr(1,b.size()-1);
    cout<<sub<<'\n';
    string c=" My   Name  Yash ";
    cout<<c<<'\n';
    while(!c.empty()&& c.front()==' ') c.erase(c.begin());
    cout<<c<<"Test space"<<'\n';
    while(!c.empty() &&c.back()==' ') c.pop_back();
    cout<<c<<"Test space"<<'\n';
    string d;
    for(int i=0;i<c.length();i++){
        if(c[i]==' '&&c[i-1]==' '){
            continue;
        }
        d+=c[i];
    }
    cout<<d<<'\n';
    string e;
    string f;
    for(int i=d.size()-1;i>=0;i--){

        if(d[i]==' '){
            string g;
            for(int i=f.size()-1;i>=0;i--){
                g+=f[i];
            }
            e+=g;
            e+=' ';
            f.erase();
            g.erase();
        }
        else {
            f += d[i];

            if (i == 0 && d[i] != ' ') {
                string g;
                for(int i=f.size()-1;i>=0;i--){
                    g+=f[i];
                }
                e+=g;
            }
        }
    }
    cout<<e;
}
