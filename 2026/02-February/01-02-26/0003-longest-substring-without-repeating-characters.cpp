/*
 * LeetCode 3 · Longest Substring Without Repeating Characters · Medium
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 *
 * Pattern : Sliding Window
 * Solved  : 01 Feb 2026
 * Time    : O(N) or O(N^2) depending on find/erase implementation, Space: O(N)
 * Space   : O(N)
 */

// LeetCode 3 - Longest Substring Without Repeating Characters
// Solved on: 2026-02-01
// Topic: String
// Approach: Sliding Window
// Time: O(N) or O(N^2) depending on find/erase implementation, Space: O(N)

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
