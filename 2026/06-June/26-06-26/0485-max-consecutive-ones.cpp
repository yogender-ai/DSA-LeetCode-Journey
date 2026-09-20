/*
 * LeetCode 485 · Max Consecutive Ones · Easy
 * https://leetcode.com/problems/max-consecutive-ones/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int a=0;
        int b;
        vector<int>ans;
        for(auto x:nums){
            if(x==1){
                a++;
            }
            else{
                ans.push_back(a);
                a=0;
            }
        }
        ans.push_back(a);
        b =*max_element(ans.begin(),ans.end());
        return b;
    }
};
