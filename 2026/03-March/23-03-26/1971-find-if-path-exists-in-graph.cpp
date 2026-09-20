/*
 * LeetCode 1971 · Find if Path Exists in Graph · Easy
 * https://leetcode.com/problems/find-if-path-exists-in-graph/
 *
 * Pattern : Graphs & Search
 * Solved  : 23 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<list<int>>l(n);
        if (source == destination) return true;
        for(auto& x:edges){
            l[x[0]].push_back(x[1]);
            l[x[1]].push_back(x[0]);

        }
        return bfs(l,source,destination);
    }
    bool bfs(vector<list<int>>&edges,int source,int destination){
        queue<int>q;
        vector<int>vis(edges.size(),0);
        q.push(source);
        vis[source]=1;
        while(!q.empty()){
            int u=q.front();
            q.pop();
            for(int x:edges[u]){
                if(x==destination){
                    return true;
                }
                if (!vis[x]) {
                    vis[x] = 1;
                    q.push(x);
                }
            }
        }
        return 0;
    }
};
