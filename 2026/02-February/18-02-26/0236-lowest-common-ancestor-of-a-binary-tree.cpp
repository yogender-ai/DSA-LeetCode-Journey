/*
 * LeetCode 236 · Lowest Common Ancestor of a Binary Tree · Medium
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 *
 * Pattern : Trees & BST
 * Solved  : 18 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==nullptr || root==p|| root==q) return root;
        TreeNode* left=lowestCommonAncestor(root->left,p,q);
        TreeNode* right=lowestCommonAncestor(root->right,p,q);
        if(left!=nullptr &&right!=nullptr) return root;
        else if(right==nullptr) return left;
        else if(left==nullptr)return right;
        else if(left==nullptr && right==nullptr) return nullptr;
        return nullptr;

    }
};
