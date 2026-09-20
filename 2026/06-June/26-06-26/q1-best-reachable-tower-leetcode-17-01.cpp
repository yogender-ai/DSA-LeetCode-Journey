/*
 * DSA Lesson · Q1. Best Reachable Tower©Leetcode(17 01)
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> bestTower(vector<vector<int>>& towers, vector<int>& center, int radius) {
        vector<int>reach;
        vector<int>cor;
        for(int i=0;i<towers.size();i++){
            int a=towers[i][0];
            int b=towers[i][1];
            int c=towers[i][2];
            int x=center[0];
            int y=center[1];
            int ans=abs(a-x)+abs(b-y);
            if(ans<=radius){
                reach.push_back(a);
                reach.push_back(b);
                cor.push_back(c);
            }

        }
        if(reach.size()==0){
            return {-1,-1};
        }


        vector<int>g;

        int max=*max_element(cor.begin(),cor.end());
        int p=INT_MAX;
        int q=INT_MAX;

        for(int i=0;i<cor.size();i++){
            int x, y;
            if(max==cor[i]){
                x=reach[2*i];
                y=reach[2*i+1];
                if(x<p || (x==p && y<q)){
                    p=x;
                    q=y;
                }
            }




        }
        g.push_back(p);
        g.push_back(q);
        return g;
    }
};©leetcode
