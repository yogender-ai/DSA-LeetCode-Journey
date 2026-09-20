/*
 * DSA Lesson · Inorder
 *
 * Pattern : Data Structures & Algorithms
 * Written : 22 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include<queue>
using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
    Node(int value){
        data=value;
        left=nullptr;
        right=nullptr;
    }
};
class tree{
    Node* root=nullptr;
public:

void Insert(int value){
    if(root==nullptr){
        root=new Node(value);
        return;
    }
    queue<Node*>q;
    q.push(root);
    while(!q.empty()){
        Node* curr=q.front();
        q.pop();
        if(curr->left!=nullptr){
            q.push(curr->left);
        }
        else{
            curr->left= new Node(value);
            return;
        }
        if(curr->right!=nullptr){
            q.push(curr->right);
        }
        else{
            curr->right=new Node(value);
            return;
        }
    }

}
void preorder(Node* root){
    if(root==nullptr) {
        return;
    }
    cout<<root->data<<'\n';
    preorder(root->left);
    preorder(root->right);
}
void inorder(){
    preorder(root);
    return;
}
void leafs(Node* root){
    if(root==nullptr){
        return;
    }
    if(root->left==nullptr || root->right==nullptr){
        cout<<root->data;
    }
    leafs(root->left);
    leafs(root->right);
}
void leafs(){
    leafs(root);
}
};
int main(){
    tree n;
    n.Insert(1);
    n.Insert(2);
    n.Insert(3);
    n.Insert(4);
    n.Insert(5);
    n.Insert(6);
    n.Insert(7);
    n.Insert(8);
    n.Insert(9);
    n.leafs();


}
