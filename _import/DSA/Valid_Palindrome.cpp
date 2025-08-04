/*
Problem: Valid Palindrome
Link: https://leetcode.com/problems/valid-palindrome/

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Examples:
1. Input: s = "A man, a plan, a canal: Panama"
   Output: true
   Explanation: "amanaplanacanalpanama" is a palindrome.

2. Input: s = "race a car"
   Output: false
   Explanation: "raceacar" is not a palindrome.

3. Input: s = " "
   Output: true
   Explanation: After removing non-alphanumeric characters, string is "".
                Empty string is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

Approach:
1. Filter out all non-alphanumeric characters and convert the remaining ones to lowercase.
2. Use two-pointer technique:
   - One pointer starts from the beginning, another from the end.
   - Compare characters while moving inward.
3. If all characters match, it is a palindrome.

Time Complexity:
- O(n) — We scan the string once to clean it, and once to compare.
Space Complexity:
- O(n) — We store the cleaned version of the string.

*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string cleaned = "";
        
        
        for (char c : s) {
            if (isalnum(c)) {
                cleaned += tolower(c);
            }
        }

        
        int left = 0, right = cleaned.size() - 1;
        while (left < right) {
            if (cleaned[left] != cleaned[right]) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
};



