/*
 * DSA Lesson · Treesmaster
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

/*#include<iostream>
#include<queue>
using namespace std;
int main() {
    queue<int>v;
    v.push(3);
    v.push(4);
    v.push(5);
    v.push(6);
    cout<<v.front();
    v.pop();
    cout<<v.front();
}*/
#include <iostream>
#include <queue>
using namespace std;
struct node {
    int data;
    node* left;
    node* right;
    node(int value) {
        data=value;
        left=right=nullptr;
    }
};
class tree {
public:
    node* root;
    tree() {

        root=nullptr;

    }


    void add(int v) {
        node* newnode=new node(v);
        if (!root) {
            root=newnode;
            return;
        }
        queue<node*>q;
        q.push(root);
        while (!q.empty()) {
            node* curr=q.front();
            q.pop();
            if (!curr->left) {
                curr->left=newnode;
                return;
            }
            else q.push(curr->left);
            if (!curr->right) {
                curr->right=newnode;
                return;
            }
            else q.push(curr->right);
        }



    }
    void print() {
        if (!root) return;
        queue<node*>q;
        q.push(root);
        while (!q.empty()) {
            node* curr=q.front();
            q.pop();
            cout<<curr->data<<' ';
            if (curr->left) q.push(curr->left);
            if (curr->right)q.push(curr->right);
        }
    }
    void inorder(node* curr){
        if(!curr) return;

        inorder(curr->left);
        cout << curr->data << " ";
        inorder(curr->right);
    }
    void inorder(){
        inorder(root);
    }
    void postorder(node* curr) {
        if (!curr) return;

        postorder(curr->left);


        postorder(curr->right);
        cout<<curr->data<<' ';
    }
    void postorder() {
        postorder(root);
    }
    void preorder(node* curr) {
        if (!curr) return;
        cout<<curr->data<<" ";
        preorder(curr->left);
        preorder(curr->right);
    }
    void preorder() {
        preorder(root);
    }



};
int main() {
    tree t;
    t.add(1);
    t.add(2);
    t.add(3);
    t.add(4);
    t.add(5);
    t.print();
    cout<<endl;
    t.inorder();
    cout<<endl;
    t.preorder();

}
