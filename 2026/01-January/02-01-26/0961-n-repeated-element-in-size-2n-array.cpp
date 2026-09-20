/*
 * LeetCode 961 · N-Repeated Element in Size 2N Array · Easy
 * https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 02 Jan 2026
 * Time    : O(n)
 * Space   : O(1)
 */

//optimized version
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_map<int,int>q;
        int n;
        for(auto x:nums){
            q[x]++;
            if(q[x]>1){
                return x;

            }
        }
        return -1;
        /*for(auto x:q){
            if(x.second>1){
                n=x.first;
                break;
            }
        }*/

    }
};
