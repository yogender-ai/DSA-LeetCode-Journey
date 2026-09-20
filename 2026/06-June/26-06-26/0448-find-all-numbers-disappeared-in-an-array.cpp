/*
 * LeetCode 448 · Find All Numbers Disappeared in an Array · Easy
 * https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();

        // Step 1: Mark seen numbers
        for(int i = 0; i < n; i++) {
            int index = abs(nums[i]) - 1;
            if(nums[index] > 0)
                nums[index] = -nums[index];
        }

        // Step 2: Collect missing numbers
        vector<int> ans;
        for(int i = 0; i < n; i++) {
            if(nums[i] > 0)
                ans.push_back(i + 1);
        }

        return ans;
    }
};
