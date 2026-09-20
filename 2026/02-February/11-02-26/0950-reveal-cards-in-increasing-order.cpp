/*
 * LeetCode 950 · Reveal Cards In Increasing Order · Medium
 * https://leetcode.com/problems/reveal-cards-in-increasing-order/
 *
 * Pattern : Sorting & STL
 * Solved  : 11 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        sort(deck.begin(),deck.end());
        queue<int>q;
        int n=deck.size();
        vector<int>result(n);
        for(int i=0;i<n;i++){
            q.push(i);
        }
        for(int e:deck){
            int i=q.front();//0,1,2,3,4,5,6
                            //2,3,5,7,11,13,17
            q.pop();
            result[i]=e;
            if(!q.empty()){
                q.push(q.front());
                q.pop();
            }
        }
        return result;
    }
};
