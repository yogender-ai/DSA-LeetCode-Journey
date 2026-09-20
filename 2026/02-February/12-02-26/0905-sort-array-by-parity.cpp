/*
 * LeetCode 905 · Sort Array By Parity · Easy
 * https://leetcode.com/problems/sort-array-by-parity/
 *
 * Pattern : Two Pointers
 * Solved  : 12 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int>a;
        vector<int>b;
        for(int i=0;i<nums.size();i++){
            if(nums[i]%2==0){
                a.push_back(nums[i]);
            }
            else b.push_back(nums[i]);
        }
        a.insert(a.end(),b.begin(),b.end());
        return a;
    }
};
