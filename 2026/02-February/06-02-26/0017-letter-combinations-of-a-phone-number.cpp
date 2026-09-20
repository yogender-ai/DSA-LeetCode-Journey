/*
 * LeetCode 17 · Letter Combinations of a Phone Number · Medium
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 06 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<string> s(string a){
        vector<string>q={"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        vector<string> qq;
        for(int i=0;i<a.length();i++){
            int w=a[i]-'0';
            qq.push_back(q[w]);
        }
        
        return qq;
    }
     void help(int idx, vector<string>& d, string curr, vector<string>& ans) {
        if (idx == d.size()) {
            ans.push_back(curr);
            return;
        }

        for (int j = 0; j < d[idx].size(); j++) {
            help(idx + 1, d, curr + d[idx][j], ans);
        }
    }
    vector<string> letterCombinations(string digits) {
        vector<string>ans;
        string curr="";
        vector<string>q=s(digits);
        help(0,q,curr,ans);
        return ans;
    }
};
