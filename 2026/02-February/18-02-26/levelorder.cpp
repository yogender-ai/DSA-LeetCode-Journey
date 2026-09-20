/*
 * DSA Lesson · Levelorder
 *
 * Pattern : Data Structures & Algorithms
 * Written : 18 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include <vector>
#include<queue>
using namespace std;

//Node Structure
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int x) {
        data = x;
        left = right = NULL;
    }
};

vector<int>levelOrder(Node* root,vector<int>&res){
    if(root==nullptr) return res;

    queue<Node*>q;
    q.push(root);
    while(!q.empty()){
        int lev=q.size();
        for(int i=0;i<lev;i++){
            Node* n=q.front();
            q.pop();
            res.push_back(n->data);
            if(n->left!=nullptr){
                q.push(n->left);

            }
            if(n->right!=nullptr){
                q.push(n->right);
            }
        }


    }
    return res;

}

int main() {
    // Create binary tree
    //       1
    //      /  \
    //    2     3
    //   / \     \
    //  4   5     6
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->right = new Node(6);

    vector<int> res;
    levelOrder(root, res);

    for( int node : res)
        cout << node << " ";

    return 0;
}
