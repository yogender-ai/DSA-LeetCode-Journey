/*
 * LeetCode 215 · Kth Largest Element in an Array · Medium
 * https://leetcode.com/problems/kth-largest-element-in-an-array/
 *
 * Pattern : Sorting & STL
 * Solved  : 13 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int partition(vector<int>&a,int st,int end){
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
    int quick(vector<int>&a,int l,int r,int k){
            if(l==r) return a[l];
            int pi = partition(a,l,r);
            if(pi==k){
                return a[pi];
            }
            if(pi>k){
                return quick(a,l,pi-1,k);
            
            }
            else{
                return quick(a,pi+1,r,k);
            }
        

    }
    int findKthLargest(vector<int>& nums, int k) {
        int right=nums.size()-1;
        int r=nums.size()-k;
        int ans=quick(nums,0,right,r);
        return ans;
    }
};
