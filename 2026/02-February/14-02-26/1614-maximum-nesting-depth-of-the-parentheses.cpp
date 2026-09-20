/*
 * LeetCode 1614 · Maximum Nesting Depth of the Parentheses · Easy
 * https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
 *
 * Pattern : Stack
 * Solved  : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int maxDepth(string s) {
        int maxi=0;
        int c=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                c++;
            }
            if(s[i]==')'){
                c--;
            }
            maxi=max(maxi,c);
        }
        return maxi;
    }
};
