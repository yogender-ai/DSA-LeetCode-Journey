class Solution {
public:
    int firstUniqChar(string s) {
        // Frequency map using hashing
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Traverse string to find first character with frequency 1
        for (int i = 0; i < s.size(); i++) {
            if (freq[s[i]] == 1) {
                return i;
            }
        }

        // No unique character found
        return -1;
    }
};
