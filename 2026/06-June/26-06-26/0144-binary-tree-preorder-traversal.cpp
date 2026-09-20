/*
 * LeetCode 144 · Binary Tree Preorder Traversal · Easy
 * https://leetcode.com/problems/binary-tree-preorder-traversal/
 *
 * Pattern : Stack
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int>q;
    vector<int> preorderTraversal(TreeNode* root) {
        q.clear();
        preorder(root);
        return q;
    }
    void preorder(TreeNode* root){
        if(!root) return;
        q.push_back(root->val);
        preorder(root->left);
        preorder(root->right);
    }

};
