/*
 * LeetCode 735 · Asteroid Collision · Medium
 * https://leetcode.com/problems/asteroid-collision/
 *
 * Pattern : Stack
 * Solved  : 15 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int>s;
        vector<int>ans;
        bool d=0;
        for(int i=0;i<asteroids.size();i++){
            d=0;
            while(!s.empty()&&asteroids[i]<0&&s.top()>0){
                int n=abs(asteroids[i]);
                if(n>s.top()){
                    s.pop();
                    continue;
                }
                else if(n==s.top()){
                    s.pop();
                    d=1;
                    break;
                }
                else{
                    d=1;
                    break;
                }
                
            }
            
            if(d==0) s.push(asteroids[i]);
        }
        while(!s.empty()){
            int temp=s.top();
            ans.push_back(temp);
            s.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
