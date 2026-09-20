/*
 * DSA Lesson · Bst Traversal
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include "bst.h"
using namespace std;
void bst:: inorder(node* curr){
    if(!curr) return;
    inorder(curr->left);
    cout<<curr->data<<'\n';
    inorder(curr->right);
}
void bst:: inorder(){
    return inorder(root);
}
