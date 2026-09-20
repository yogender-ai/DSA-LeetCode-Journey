/*
 * LeetCode 100 · Same Tree · Easy
 * https://leetcode.com/problems/same-tree/
 *
 * Pattern : Trees & BST
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // both null
        if(p == NULL && q == NULL)
            return true;

        // one null, other not
        if(p == NULL || q == NULL)
            return false;

        // values different
        if(p->val != q->val)
            return false;

        // check left and right
        return isSameTree(p->left, q->left) &&
               isSameTree(p->right, q->right);
    }
};
