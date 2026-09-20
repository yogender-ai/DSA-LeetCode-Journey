/*
 * LeetCode 1365 · How Many Numbers Are Smaller Than the Current Number · Easy
 * https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int>a;
        int n=0;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums.size();j++){
                if(nums[i]>nums[j]){
                    n++;
                }
            }
            a.push_back(n);
            n=0;
        }
        return a;
    }

};
