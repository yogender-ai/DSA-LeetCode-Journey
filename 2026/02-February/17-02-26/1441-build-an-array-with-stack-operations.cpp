/*
 * LeetCode 1441 · Build an Array With Stack Operations · Medium
 * https://leetcode.com/problems/build-an-array-with-stack-operations/
 *
 * Pattern : Stack
 * Solved  : 17 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string>a;
        int j=0;
        int q=target.size();

        for(int i=1;i<=target[q-1];i++){
            if(j<q&&target[j]==i){
                a.push_back("Push");
                j++;
            }
            else{
                a.push_back("Push");
                a.push_back("Pop");
            }

        }
        return a;
    }
};
