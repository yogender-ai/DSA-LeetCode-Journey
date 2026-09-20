/*
 * LeetCode 682 · Baseball Game · Easy
 * https://leetcode.com/problems/baseball-game/
 *
 * Pattern : Stack
 * Solved  : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int calPoints(vector<string>& o) {
        stack<int>s;
        for(int i=0;i<o.size();i++){
            if(o[i]=="+"){
                if(!s.empty()){
                    int sum=0;
                    int first=s.top();
                    s.pop();
                    sum=sum+first+s.top();
                    s.push(first);
                    s.push(sum);
                }
            }
            else if(o[i]=="C"){
                s.pop();
            }
            else if(o[i]=="D"){
                int sum=s.top()*2;
                s.push(sum);
            }
            else{
                
                s.push(stoi(o[i]));
            }
        }
        int sum=0;
        while(!s.empty()){
            sum+=s.top();
            s.pop();
        }
        return sum;

    }
};
