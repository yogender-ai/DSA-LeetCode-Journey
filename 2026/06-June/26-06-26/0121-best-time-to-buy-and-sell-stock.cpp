/*
 * LeetCode 121 · Best Time to Buy and Sell Stock · Easy
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 *
 * Pattern : Dynamic Programming
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            minPrice = min(minPrice, price);
            maxProfit = max(maxProfit, price - minPrice);
        }

        return maxProfit;
    }
};
