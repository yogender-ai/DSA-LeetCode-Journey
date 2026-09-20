/*
 * LeetCode 1011 · Capacity To Ship Packages Within D Days · Medium
 * https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
 *
 * Pattern : Binary Search
 * Solved  : 01 Feb 2026
 * Time    : O(n * log(sum(weights))), Space: O(1)
 * Space   : O(1)
 */

// LeetCode 1011 - Capacity To Ship Packages Within D Days
// Solved on: 2026-02-01
// Topic: Binary Search, Array
// Approach: Binary Search on Answer
// Time: O(n * log(sum(weights))), Space: O(1)


class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int min=weights[0];
        for(int i=0;i<weights.size();i++){
            if(min<weights[i]){
                min=weights[i];
            }
        }
        
        int max=0;
        for(int i=0;i<weights.size();i++){
            max+=weights[i];
        }
        int left=min;
        int right=max;
        int ans=0;
        while(left<=right){
            int mid=left+(right-left)/2;
            
            if(m(weights,mid)<=days){
                ans=mid;
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        return ans;

    }
    int m(vector<int>w,int n){
        int sum=0;
        int count=0;
        for(int i=0;i<w.size();){
            for(int j=i;sum<=n&&j<w.size();j++){
                sum+=w[j];
                if(sum>n){
                    sum=sum-w[j];
                    break;
                }
                i++;
            }
            count++;
            sum=0;
        }
        return count;
    }
};
