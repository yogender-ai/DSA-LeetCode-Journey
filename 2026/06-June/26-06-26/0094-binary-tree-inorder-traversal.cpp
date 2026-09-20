/*
 * LeetCode 94 · Binary Tree Inorder Traversal · Easy
 * https://leetcode.com/problems/binary-tree-inorder-traversal/
 *
 * Pattern : Stack
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int>q;
    vector<int> inorderTraversal(TreeNode* root) {
        inorder(root);
        return q;
    }
    void inorder(TreeNode* root){
        if(!root) return ;
        inorder(root->left);;
        q.push_back(root->val);
        inorder(root->right);
    }
};
