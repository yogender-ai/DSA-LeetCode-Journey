"""
LeetCode 1 · Two Sum · Easy
https://leetcode.com/problems/two-sum/

Pattern : Arrays & Hashing
Solved  : 24 Sep 2026
Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
Space   : O(1) · Memory: 19.7 MB (Beats 95.4%)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[] 
        left=0
        right=len(nums)-1
        q=sorted(nums)
        for i,num in enumerate(q):
            sum = q[left]+q[right]
            if sum ==target:
                ind=nums.index(q[left])
                a.append(ind)
                nums[ind]= None
                
                a.append(nums.index(q[right]))
                break
            if sum>target:
                right-=1
            else:
                left+=1
        return a
