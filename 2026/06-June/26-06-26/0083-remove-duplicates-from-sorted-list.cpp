/*
 * LeetCode 83 · Remove Duplicates from Sorted List · Easy
 * https://leetcode.com/problems/remove-duplicates-from-sorted-list/
 *
 * Pattern : Data Structures & Algorithms
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr = head;

        while (curr != NULL && curr->next != NULL) {
            if (curr->val == curr->next->val) {
                // skip duplicate node
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }

        return head;
    }
};
