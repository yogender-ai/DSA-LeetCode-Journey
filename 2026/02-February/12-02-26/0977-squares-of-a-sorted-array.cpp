/*
 * LeetCode 977 · Squares of a Sorted Array · Easy
 * https://leetcode.com/problems/squares-of-a-sorted-array/
 *
 * Pattern : Two Pointers
 * Solved  : 12 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    /*int partition(vector<int>&a,int st,int end){
        int i=st-1,idx=a[end];
        for(int j=st;j<end;j++){
            if(a[j]<idx){
                i++;
                swap(a[i],a[j]);
            }
        }
        i++;
        swap(a[i],a[end]);
        return i;
    }
    void quick(vector<int>&a,int l,int r){
        if(l<r){
            
            int pi=partition(a,l,r);
            quick(a,l,pi-1);
            quick(a,pi+1,r);
        }
    }*/
    vector<int> sortedSquares(vector<int>& nums) {
        for(int i=0;i<nums.size();i++){
            nums[i]=nums[i]*nums[i];
        }
        sort(nums.begin(),nums.end());
        return nums;

    }
};
