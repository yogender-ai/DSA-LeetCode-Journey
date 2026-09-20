/*
 * DSA Lesson · Bst Deletion
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include"bst.h"
using namespace std;
node* bst::succ(node* rooty){
    //if(rooty == nullptr || rooty->left == nullptr)
      //  return nullptr;

    node* newnode=rooty->left;
    while(newnode->right!=nullptr){
        newnode=newnode->right;
    }
    return newnode;
}
node*bst:: deletion(node* curr,int value){
    if(!curr)return curr;
    if(curr->data>value){
        curr->left=deletion(curr->left,value);
    }
    else if(curr->data<value){
        curr->right=deletion(curr->right,value);
    }
    else{
        if(curr->left==nullptr){
            node* temp=curr->right;
            delete curr;
            return temp;
        }
        if(curr->right==nullptr){
            node* temp=curr->left;
            delete curr;
            return temp;
        }
        node* successor=succ(curr);
        curr->data=successor->data;
        curr->left= deletion(curr->left,successor->data);


    }
    return curr;
}
void bst:: deletion(int value){
    root=deletion(root,value);
}
