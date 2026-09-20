/*
 * LeetCode 1791 · Find Center of Star Graph · Easy
 * https://leetcode.com/problems/find-center-of-star-graph/
 *
 * Pattern : Data Structures & Algorithms
 * Solved  : 24 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        int n=0;
        for(auto e:edges){
            n=max(n,max(e[0],e[1]));
        }
        vector<list<int>>g(n+1);
        for(auto x:edges){
            g[x[0]].push_back(x[1]);
            g[x[1]].push_back(x[0]);
        }

        for(int i=1;i<=n;i++){
            if(g[i].size()==n-1){
                return i;
            }
        }
        return -1;



    }
};
