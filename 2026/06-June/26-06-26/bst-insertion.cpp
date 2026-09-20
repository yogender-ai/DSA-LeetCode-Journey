/*
 * DSA Lesson · Bst Insertion
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include "bst.h"
using namespace std;

    /*node(int value){
        data=value;
        left=nullptr;
        right=nullptr;
    }*/
    //Initializer list method
    node::node(int value):data(value),left(nullptr),right(nullptr){};// member Intialization
    node* bst:: insert(node* root,int value){ //We can use value as variable name again because of scope
        if(!root){
            root=new node(value);
            return root;
        }
        if(root->data>value){
            root->left=insert(root->left,value);
        }
        else{
            root->right=insert(root->right,value);
        }
        return root;
    }
    bst::bst():root(nullptr){};
    void bst:: insert(int value){
        root=insert(root,value);
    }

