/*
 * LeetCode 645 · Set Mismatch · Easy
 * https://leetcode.com/problems/set-mismatch/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int>a;
        unordered_set<int>b;
        int temp;
        for(auto x:nums){
            auto it=b.insert(x);

            if(!it.second){
                temp=x;


            }

        }
        int missing = -1;
        int n = nums.size();

        for(int i = 1; i <= n; i++) {
            if(b.find(i) == b.end()) {
                missing = i;
                break;
            }
        }

        a.push_back(temp);
        a.push_back(missing);
        return a;

    }
};
