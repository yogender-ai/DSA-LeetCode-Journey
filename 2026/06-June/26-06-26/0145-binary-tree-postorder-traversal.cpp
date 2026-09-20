/*
 * LeetCode 145 · Binary Tree Postorder Traversal · Easy
 * https://leetcode.com/problems/binary-tree-postorder-traversal/
 *
 * Pattern : Stack
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    vector<int>q;
    vector<int> postorderTraversal(TreeNode* root) {

        postorder(root);
        return q;
    }
    void postorder(TreeNode* root){
        if(!root) return;
        postorder(root->left);
        postorder(root->right);
        q.push_back(root->val);

    }
};
