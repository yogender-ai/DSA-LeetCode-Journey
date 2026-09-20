/*
 * LeetCode 414 · Third Maximum Number · Easy
 * https://leetcode.com/problems/third-maximum-number/
 *
 * Pattern : Sorting & STL
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int thirdMax(vector<int>& nums) {
        long long first = LLONG_MIN;
        long long second = LLONG_MIN;
        long long third = LLONG_MIN;

        for(int x : nums){
            if(x == first || x == second || x == third)
                continue;

            if(x > first){
                third = second;
                second = first;
                first = x;
            }
            else if(x > second){
                third = second;
                second = x;
            }
            else if(x > third){
                third = x;
            }
        }

        if(third == LLONG_MIN)
            return first;
        return third;
    }

};
