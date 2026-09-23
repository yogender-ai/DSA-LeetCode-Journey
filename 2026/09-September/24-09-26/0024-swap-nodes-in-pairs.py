"""
LeetCode 24 · Swap Nodes in Pairs · Medium
https://leetcode.com/problems/swap-nodes-in-pairs/

Pattern : Data Structures & Algorithms
Solved  : 24 Sep 2026
Time    : O(n) · Runtime: 13 ms (Beats 0.2%)
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
        if head==None or head.next==None:
            return head
        temp=head
        head=head.next
        
        temp.next= self.swapPairs(head.next)
        head.next=temp
        return head
