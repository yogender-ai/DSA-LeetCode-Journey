/*
 * LeetCode 3314 · Construct the Minimum Bitwise Array I · Easy
 * https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
 *
 * Pattern : Bit Manipulation
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;

        for(int n : nums) {
            int found = -1;

            for(int x = 0; x <= n; x++) {
                if( (x | (x + 1)) == n ) {
                    found = x;
                    break;   // first = smallest
                }
            }

            ans.push_back(found);
        }

        return ans;
    }
};
