/*
 * DSA Lesson · Graph Everything
 *
 * Pattern : Data Structures & Algorithms
 * Written : 09 Apr 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<vector>
#include<list>
#include<queue>
using namespace std;
class Graph{
    int raw;
    vector<vector<int>>matrix;
    vector<vector<int>>li_st;
public:
    Graph(int raw){
        this->raw=raw;
        matrix=vector<vector<int>>(raw,vector<int>(raw,0));
        li_st.resize(raw);
    }

    void matrix_i(int u,int v){
        matrix[u][v]=1;
        matrix[v][u]=1;
    }
    void adjacency_i(){
        for(int i=0;i<raw;i++){
            for(int j=0;j<raw;j++){
                if(matrix[i][j]==0){
                    continue;
                }
                else{

                    li_st[i].push_back(j);

                }
            }
        }
    }
    void bfs_m(int v) {
        queue<int> q;
        q.push(v);
        vector<int> vis(raw,0);
        vis[v]=1;
        cout<<"Matrix: "<<endl;
        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (int i = 0; i < raw; i++)
            {
                if(matrix[u][i]==1&&vis[i]==0){
                    q.push(i);
                    vis[i]=1;
                    cout<<'{'<<u<<','<<i<<'}'<<' ';
                }

            }

        }
    }
    void bfs_l(int v){
        cout<<"BFS_Adjacency_list: "<<endl;
        queue<int>q;
        q.push(v);
        vector<int>vis(raw,0);
        vis[v]=1;
        while(!q.empty()){
            int u=q.front();
            q.pop();
            cout<<u<<' ';
            for(auto x:li_st[u]){
                if(vis[x]!=1){
                    q.push(x);
                    vis[x]=1;

                }
            }
        }
    }
};
int main(){
    Graph obj(4);
    obj.matrix_i(0,1);
    obj.matrix_i(1,2);
    obj.matrix_i(0,2);
    obj.matrix_i(2,3);

    obj.bfs_m(0);
    obj.adjacency_i();
    cout<<endl;
    obj.bfs_l(0);

}

