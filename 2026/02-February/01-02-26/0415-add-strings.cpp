/*
 * LeetCode 415 · Add Strings · Easy
 * https://leetcode.com/problems/add-strings/
 *
 * Pattern : Strings
 * Solved  : 01 Feb 2026
 * Time    : O(max(N, M)), Space: O(max(N, M))
 * Space   : O(max(N, M))
 */

// LeetCode 415 - Add Strings
// Solved on: 2026-02-01
// Topic: Math, String
// Approach: Element-wise Addition (Simulation)
// Time: O(max(N, M)), Space: O(max(N, M))

class Solution {
public:
    string addStrings(string num1, string num2) {
        string ans="";
        int c=0;
        
        for(int i=num1.size()-1,j=num2.size()-1;i>=0||j>=0;i--,j--){
            int a=0,b=0;
            if(i>=0){

            a=num1[i]-'0';
            }
            if(j>=0){

            b=num2[j]-'0';
            }
            int sum=a+b+c;
            c=sum/10;
            sum=sum%10;
            string s=to_string(sum);
            ans+=s;
            s.clear();

        }
        if(c!=0){
            ans+='1';
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
