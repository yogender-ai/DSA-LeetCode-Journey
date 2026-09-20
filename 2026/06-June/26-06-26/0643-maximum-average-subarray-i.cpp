/*
 * LeetCode 643 · Maximum Average Subarray I · Easy
 * https://leetcode.com/problems/maximum-average-subarray-i/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double sum=0;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        double ans=sum;
        for(int i=k;i<nums.size();i++){
            sum+=nums[i];
            sum-=nums[i-k];
            ans=max(sum,ans);
        }

        return ans/k;
    }
};
