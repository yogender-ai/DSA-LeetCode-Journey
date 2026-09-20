/*
 * LeetCode 844 · Backspace String Compare · Easy
 * https://leetcode.com/problems/backspace-string-compare/
 *
 * Pattern : Two Pointers
 * Solved  : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char>a;
        stack<char>b;
        for(int i=0;i<s.size();i++){
            if(s[i]=='#'){
                if(!a.empty()){
                    a.pop();
                }
            }
            else{
                a.push(s[i]);
            }
           
        }
        for(int i=0;i<t.size();i++){
            if(t[i]=='#'){
                if(!b.empty()){
                    b.pop();
                }
            }
            else b.push(t[i]);
        }
        string q="";
        string w="";
        while(!a.empty()){
            q+=a.top();
            a.pop();
        }
        while(!b.empty()){
            w+=b.top();
            b.pop();
        }
        if(q==w){
            return 1;
        }
        else return 0;

    }
};
