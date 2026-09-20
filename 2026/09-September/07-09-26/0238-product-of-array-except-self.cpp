/*
 * LeetCode 238 · Product of Array Except Self · Medium
 * https://leetcode.com/problems/product-of-array-except-self/
 *
 * Pattern : Prefix Sum
 * Solved  : 02 Feb 2026
 * Time    : O(n), Space: O(1)
 * Space   : O(1)
 */

// LeetCode 238 - Product of Array Except Self
// Solved on: 2026-02-03
// Topic: Array, Prefix Sum
// Approach: Counting Zeros
// Time: O(n), Space: O(1)

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>a;
        int check=0;
        int m=1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                check++;
                continue;
            }
            m=m*nums[i];
            
        }
        if(check==0){
            for(int i=0;i<nums.size();i++){
                int b=m/nums[i];
                a.push_back(b);
            }
        }
        else{
            for(int i=0;i<nums.size();i++){
                if(check>1){
                    a.push_back(0);
                }
                else if(nums[i]==0){
                    a.push_back(m);
                }else{
                    a.push_back(0);
                }
            }
        }
        return a;
        
    }
};
