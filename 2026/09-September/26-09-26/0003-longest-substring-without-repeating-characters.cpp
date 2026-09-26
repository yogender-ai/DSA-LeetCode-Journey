/*
 * LeetCode 3 · Longest Substring Without Repeating Characters · Medium
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * Pattern : Sliding Window
 * Solved  : 26 Sep 2026
 * Time    : O(n) · Runtime: 27 ms (Beats 69.5%)
 * Space   : O(1) · Memory: 17.8 MB (Beats 93.7%)
 */

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
         int count =0;
         string ans="";
         int m=0;
         for(int i=0;i<s.size();i++){
            size_t temp=ans.find(s[i]);
            if(temp==string::npos){
                ans+=s[i];
                
            }
            else{
                
                ans.erase(0,temp+1);
                
                
                ans+=s[i];
                
               


            }
            count=ans.size();
            m=max(m,count);
        }
        
        return m;
    }
};
