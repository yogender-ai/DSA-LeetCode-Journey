/*
 * LeetCode 20 · Valid Parentheses · Easy
 * https://leetcode.com/problems/valid-parentheses/
 *
 * Pattern : Stack
 * Solved  : 10 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool isValid(string s) {
        stack<char>a;

        for(int i=0;i<s.size();i++){
            if(s[i]=='('||s[i]=='{'||s[i]=='['){
                a.push(s[i]);
            }
            else{
                if(a.empty()){
                    return 0;
                }
                else if(s[i]==')'){
                    if(a.top()=='('){
                        a.pop();
                    }
                    else{
                        return 0;
                    }
                }
                else if(s[i]=='}'){
                    if(a.top()=='{'){
                        a.pop();
                    }
                    else return 0;
                }
                else{
                    if(a.top()=='['){
                        a.pop();
                    }
                    else return 0;
                }
            }
        }
        if(a.empty()){
            return 1;

        }
        else return 0;
    }
};
