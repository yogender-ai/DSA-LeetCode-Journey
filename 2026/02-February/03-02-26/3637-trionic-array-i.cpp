/*
 * LeetCode 3637 · Trionic Array I · Easy
 * https://leetcode.com/problems/trionic-array-i/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 03 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int count=0;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[0]>=nums[1]||nums.size()<3||nums[i]==nums[i+1]){
                return 0;
            }
            if(count==3 &&nums[i]>nums[i+1]){
                return 0;
            }
            if(nums[i]<nums[i+1]){

                if(count==0||count==2){
                    count++;
                }
            }
            else if(nums[i]>nums[i+1]&&count==1){
                count++;
                
            }
            
            else {
                
                continue;
            }
        }
        if(count==3){
            return 1;
        }
        else{
            cout<<count;
            return 0;
        }
    }
};
