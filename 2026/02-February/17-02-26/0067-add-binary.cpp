/*
 * LeetCode 67 · Add Binary · Easy
 * https://leetcode.com/problems/add-binary/
 *
 * Pattern : Bit Manipulation
 * Solved  : 17 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    string addBinary(string a, string b) {
        int q=a.size()-1;
        int w=b.size()-1;
        char carry=0;
        string ans="";
        while (q >= 0 || w >= 0 || carry) {
            int sum = carry;

            if (q >= 0 && a[q] == '1') sum++;
            if (w >= 0 && b[w] == '1') sum++;

            ans.push_back((sum % 2) + '0');
            carry = sum / 2;

            q--;
            w--;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
