/*
 * LeetCode 31 · Next Permutation · Medium
 * https://leetcode.com/problems/next-permutation/
 *
 * Pattern : Two Pointers
 * Solved  : 07 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:

    void nextPermutation(vector<int>& nums) {
        int i=nums.size();
        if(i<=1) return;
        int j=i-2;
        while(j>=0&&nums[j]>=nums[j+1]){
            j--;
        }
        if(j>=0){
            int k=i-1;
            while(k>j){
                
                if(nums[j]<nums[k]){
                    swap(nums[j],nums[k]);
                    break;
                }
                k--;
            }

        }
        reverse(nums.begin()+j+1,nums.end());

        
            
        
    }   
};
