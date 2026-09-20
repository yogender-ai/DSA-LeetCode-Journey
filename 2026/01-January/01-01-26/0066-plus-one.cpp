/*
 * LeetCode 66 · Plus One · Easy
 * https://leetcode.com/problems/plus-one/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 01 Jan 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for(int i=digits.size()-1;i>=0;i--){
            if(digits[i]<9){
                digits[i]++;
                return digits;
            }
            digits[i]=0;
        }
        digits.insert(digits.begin(),1);
        return digits;
    }
};
