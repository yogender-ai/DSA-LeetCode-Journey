/*
 * LeetCode 32 · Longest Valid Parentheses · Hard
 * https://leetcode.com/problems/longest-valid-parentheses/
 *
 * Pattern : Stack
 * Solved  : 11 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int>a;
        int maxi=0;
        a.push(-1);
        
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                a.push(i);
            }
            else{
                a.pop();
                if(a.empty()){
                    a.push(i);
                }
                else{
                    maxi=max(maxi,i-a.top());
                }
            }
        }
        return maxi;
    }
};
