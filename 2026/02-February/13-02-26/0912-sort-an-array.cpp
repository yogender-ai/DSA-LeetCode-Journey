/*
 * LeetCode 912 · Sort an Array · Medium
 * https://leetcode.com/problems/sort-an-array/
 *
 * Pattern : Sorting & STL
 * Solved  : 13 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int partition(vector<int>&a,int st,int end){
        int pivotIndex = st + rand() % (end - st + 1);
        swap(a[pivotIndex], a[end]);   
        int idx=st-1,pi=a[end];
        for(int i=st;i<end;i++){
            if(a[i]<pi){
                idx++;
                swap(a[i],a[idx]);
            }
        }
        idx++;
        swap(a[idx],a[end]);
        return idx;
    }
    void quick(vector<int>&a,int l,int r){
        if(l<r){
            int pi=partition(a,l,r);
            quick(a,l,pi-1);
            quick(a,pi+1,r);
        }
    }
    vector<int> sortArray(vector<int>& nums) {
        int r=nums.size()-1;
        quick(nums,0,r);
        return nums;
    }
};
