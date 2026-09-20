/*
 * LeetCode 3838 · Weighted Word Mapping · Easy
 * https://leetcode.com/problems/weighted-word-mapping/
 *
 * Pattern : Strings
 * Solved  : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string ans="";
        for(string w:words){
            int sum=0;
            for(char ch:w){
                sum+=weights[ch-'a'];
            }
            int modulo=sum%26;
            char m='z'-modulo;
            ans.push_back(m);
        }
        return ans;
    }
};
