/*
 * LeetCode 231 · Power of Two · Easy
 * https://leetcode.com/problems/power-of-two/
 *
 * Pattern : Bit Manipulation
 * Solved  : 02 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n==1){
            return 1;
        }
        else if(n%2!=0 ||n==0){
            return 0;
        }
        else{

            while(n!=1){
                if(n%2!=0){
                    return 0;
                }
                n=n/2;
                
            }
            return 1;
            
        }
    }
};
