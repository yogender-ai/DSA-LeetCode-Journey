/*
 * LeetCode 860 · Lemonade Change · Easy
 * https://leetcode.com/problems/lemonade-change/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 08 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
         int f=0;
         int t=0;
         int tw=0;
         for(int i=0;i<bills.size();i++){
            if(bills[i]==5){
                f++;

            }
            else if(bills[i]==10){
                if(f!=0){
                    f--;
                    t++;

                }
                else{
                    return 0;
                }
            }
            else{
                if(t!=0&&f!=0){
                    t--;
                    f--;

                }
                else if(f>=3){
                    f=f-3;
                }
                else{
                    return 0;
                }
            }
         }
         return 1;
    }
};
