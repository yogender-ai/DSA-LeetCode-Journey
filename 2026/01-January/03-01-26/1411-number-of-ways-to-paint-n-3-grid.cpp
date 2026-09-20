/*
 * LeetCode 1411 · Number of Ways to Paint N × 3 Grid · Hard
 * https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
 *
 * Pattern : Dynamic Programming
 * Solved  : 03 Jan 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int numOfWays(int n) {
        const int MOD = 1e9 + 7;

        long long same = 6;
        long long diff = 6;

        for (int i = 2; i <= n; i++) {
            long long newSame = (2*same + 2*diff) % MOD;
            long long newDiff = (2*same + 3*diff) % MOD;

            same = newSame;
            diff = newDiff;
        }

        return (same + diff) % MOD;
    }
};
