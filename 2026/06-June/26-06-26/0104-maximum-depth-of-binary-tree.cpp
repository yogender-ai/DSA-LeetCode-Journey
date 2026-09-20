/*
 * LeetCode 104 · Maximum Depth of Binary Tree · Easy
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/
 *
 * Pattern : Trees & BST
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        int l=maxDepth(root->left);
        int r=maxDepth(root->right);
        return 1+max(l,r);
    }
};
