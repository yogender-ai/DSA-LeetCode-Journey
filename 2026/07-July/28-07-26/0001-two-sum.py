"""
LeetCode 1 · Two Sum · Easy
https://leetcode.com/problems/two-sum/

Pattern : Sorting + Two Pointers
Solved  : 28 Jul 2026
Time    : O(n log n)
Space   : O(n)
"""

from typing import List

# Attempt 1 — 28 Jul 2026
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        new=sorted(nums)
        while(left!=right):
            sum=new[left]+new[right]
            if(sum==target and left!=right):
                break
            elif(sum<target):
                left+=1
            else:
                right-=1
        pleft=nums.index(new[left])
        pright=nums.index(new[right])
        if pleft==pright:
            pright=nums.index(new[right],pleft+1)
        return [pleft,pright]


# Attempt 2 — 14 Aug 2026
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        left = 0
        right = len(nums) - 1
        q = sorted(nums)
        for i, num in enumerate(q):
            sum = q[left] + q[right]
            if sum == target:
                ind = nums.index(q[left])
                a.append(ind)
                nums[ind] = None

                a.append(nums.index(q[right]))
                break
            if sum > target:
                right -= 1
            else:
                left += 1
        return a
