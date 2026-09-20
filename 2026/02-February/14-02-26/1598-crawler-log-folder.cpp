/*
 * LeetCode 1598 · Crawler Log Folder · Easy
 * https://leetcode.com/problems/crawler-log-folder/
 *
 * Pattern : Stack
 * Solved  : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int minOperations(vector<string>& logs) {
        stack<string>a;
        int count=0;
        for(int i=0;i<logs.size();i++){
            if(logs[i]=="../"){
                if(!a.empty()){
                    a.pop();
                }
            }
            else if(logs[i]=="./"){
                continue;
            }
            else{
                a.push(logs[i]);
            }
        }
        while(!a.empty()){
            count++;
            a.pop();
        }
        return count;
    }
};
