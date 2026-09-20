/*
 * LeetCode 42 · Trapping Rain Water · Hard
 * https://leetcode.com/problems/trapping-rain-water/
 *
 * Pattern : Two Pointers
 * Solved  : 09 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        vector<int>left(n);
        left[0]=height[0];
        for(int i=1;i<n;i++){
            left[i]=max(left[i-1],height[i]);
           
        }
        vector<int>right(n );
        right[n-1]=height[n-1];
        for(int i=n-2;i>=0;i--){
            right[i]=max(right[i+1],height[i]);
            
        }
        int sum=0;
        for(int i=0;i<n;i++){
            int a=min(left[i],right[i]);
            int b=a-height[i];
            sum+=b;
        }
        return sum;
        
    }   
};
