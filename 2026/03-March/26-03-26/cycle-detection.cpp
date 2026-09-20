/*
 * DSA Lesson · Cycle Detection
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include <list>
#include <vector>
using namespace std;
class graph{
    vector<list<int>>net;
    int v;
public:
    graph(){
        this->v=v;
        net.resize(v);
    }
    void insert(int num1,int num2){
        net[num1].push_back(num2);
        net[num2].push_back(num2);
    }
    void bfs(){
        cout<<"BFS initializing..."<<'\n';

    }
    void dfs(vector<int>vis,int source){
        cout<<source<<" ";
        for(auto x:net){

        }
    }
};
