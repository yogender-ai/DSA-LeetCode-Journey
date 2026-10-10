/*
 * LeetCode 7 · Reverse Integer · Medium
 * https://leetcode.com/problems/reverse-integer/
 *
 * Pattern : Data Structures & Algorithms
 * Solved  : 10 Oct 2026
 * Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
 * Space   : O(1) · Memory: 8.6 MB (Beats 20.2%)
 */

class Solution {
public:
    int reverse(int x) {
        int rev = 0;

        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            // Check overflow BEFORE adding digit
            if (rev > INT_MAX/10 || (rev == INT_MAX/10 && digit > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN/10 && digit < -8)) return 0;

            rev = rev * 10 + digit;
        }

        return rev;
    }
};
