/*
 * LeetCode 102 · Binary Tree Level Order Traversal · Medium
 * https://leetcode.com/problems/binary-tree-level-order-traversal/
 *
 * Pattern : Trees & BST
 * Solved  : 18 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
void levelOrder(TreeNode* root,vector<vector<int>>&a){
    if(root==nullptr) return;
    

    int lev=0;
    queue<TreeNode*>q;
    q.push(root);
    while(!q.empty()){
         int size = q.size();
        
        vector<int>qq;

        for(int i=0;i<size;i++){
            TreeNode* n=q.front();
            q.pop();
            qq.push_back(n->val);
            if(n->left!=nullptr){
                q.push(n->left);

            }
            if(n->right!=nullptr){
                q.push(n->right);
            }
        }
         a.push_back(qq);  
    }
    

}
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>a;
        levelOrder(root,a);
        return a;
    }
};
