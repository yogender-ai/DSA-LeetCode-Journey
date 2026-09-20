/*
 * LeetCode 1390 · Four Divisors · Medium
 * https://leetcode.com/problems/four-divisors/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 04 Jan 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int ans=0;
        for(auto x:nums){
            if(d(x).size()==4){
                for(auto t:d(x)){
                    ans=ans+t;
                }

            }
        }
        return ans;

    }
    unordered_set<int>d(int n){
        unordered_set<int>s;
        for(int i=1;i*i<=n;i++){
            if(n%i==0){
                s.insert(i);
                if(i!=n/i){
                    s.insert(n/i);
                }
            }
        }
        return s;
    }
};
//Learn the concept that i is divided by n than n/i is also divided by n.
