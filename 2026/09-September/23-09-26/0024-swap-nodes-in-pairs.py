"""
LeetCode 24 · Swap Nodes in Pairs · Medium
https://leetcode.com/problems/swap-nodes-in-pairs/

Pattern : Data Structures & Algorithms
Solved  : 23 Sep 2026
Time    : O(n) · Runtime: 8 ms (Beats 0.2%)
Space   : O(1) · Memory: 12.5 MB (Beats 43.6%)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head
        trigger=1
        if head==None:
            return 
        while temp.next!=None:

            if trigger%2!=0:
                w=temp.val
                temp.val=temp.next.val
                temp.next.val=w
            trigger+=1
            temp=temp.next
        return head
