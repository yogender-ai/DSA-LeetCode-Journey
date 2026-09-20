/*
 * LeetCode 3833 · Count Dominant Indices · Easy
 * https://leetcode.com/problems/count-dominant-indices/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 08 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int dominantIndices(vector<int>& nums) {
        int n=nums.size();
        int count=0;
        for(int i=0;i<n-1;i++){
            int sum=0;
            int iter=0;
            for(int j=i+1;j<n;j++){
                sum+=nums[j];
                iter++;
            }
            double avg=0;
            if(iter!=0){
                
                avg=(double)sum/iter;
            }
            
            if(nums[i]>avg){
                count++;
            }
            
        }
        return count;
    }
};
