/*
 * LeetCode 383 · Ransom Note · Easy
 * https://leetcode.com/problems/ransom-note/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int i=0;
        for(auto x:ransomNote){
            auto pos =magazine.find(x);
            if(pos==string::npos){
                return 0;
            }
            magazine.erase(pos,1);
        }
        return 1;
    }
};
