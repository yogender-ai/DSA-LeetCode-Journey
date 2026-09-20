/*
 * LeetCode 167 · Two Sum II - Input Array Is Sorted · Medium
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 *
 * Pattern : Two Pointers
 * Solved  : 20 May 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0;
        int r=numbers.size()-1;
        int i1=0;
        int i2=0;
        while(l<r){
            int sum=numbers[l]+numbers[r];
            if(sum==target){
                return {l+1,r+1};
            }
            else if(sum<target){
                l++;
            }
            else{
                r--;
            }
        }
        return {};
        
    }
};
