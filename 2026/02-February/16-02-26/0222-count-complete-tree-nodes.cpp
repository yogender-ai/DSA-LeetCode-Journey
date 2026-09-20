/*
 * LeetCode 222 · Count Complete Tree Nodes · Medium
 * https://leetcode.com/problems/count-complete-tree-nodes/
 *
 * Pattern : Binary Search
 * Solved  : 16 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    int countNodes(TreeNode* root) {
        if(root==NULL) return 0;
        int left=countNodes(root->left);
        int right=countNodes(root->right);
        return right+left+1;
    }
};
