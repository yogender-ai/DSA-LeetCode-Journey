/*
 * DSA Lesson · Graph
 *
 * Pattern : Data Structures & Algorithms
 * Written : 08 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<list>
#include<vector>
#include<iostream>
using namespace std;
class graph{
    int n;
    vector<list<int>>arr;

public:

    graph(int d){
        n=d;
        arr.resize(n);
    }
    void add(int u,int v){
        arr[u].push_back(v);
        arr[v].push_back(u);
    }
    void print(){
        for(int i=0;i<n;i++){
            cout<<i<<": ";
            for(int q:arr[i]){
                cout<<q<<" ";
            }
            cout<<'\n';
        }
    }

};
int main(){
graph g(4);
g.add(0,1);
g.add(1,2);
g.add(2,3);
g.add(3,1);
g.print();

return 0;

}



