/*
 * LeetCode 1475 · Final Prices With a Special Discount in a Shop · Easy
 * https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
 *
 * Pattern : Stack
 * Solved  : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> finalPrices(vector<int>& p) {
        stack<int>s;
        for(int i=0;i<p.size();i++){
            while(!s.empty()&&p[i]<=p[s.top()]){
                int idx = s.top();
                s.pop();
                p[idx] -= p[i];
            }
            s.push(i);
        }
        return p;
    }
};
