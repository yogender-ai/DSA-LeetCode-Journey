/*
 * DSA Lesson · Binary Tree
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

//Binary Tree:- Let's Master this

#include <iostream>
#include <queue>
#include <vector>
using namespace std;
struct node {
    int data;
    node* left;
    node* right;
    node(int value) {
        data=value;
        left=nullptr;
        right=nullptr;
    }
};
class LinkedList {
    node* head=nullptr;
public:
    void insert(vector<int>ai) {
        for (auto x:ai) {
            if (!head) {
                head=new node(x);
                continue;
            }
            queue<node*>q;
            q.push(head);
            while (!q.empty()) {
                node* temp=q.front();
                q.pop();
                if (!temp->left) {
                    temp->left=new node(x);
                    break;
                }
                else q.push(temp->left);
                if (!temp->right) {
                    temp->right=new node(x);
                    break;
                }
                else q.push(temp->right);
            }
        }

    }
    void inorder(node* curr) {
        if (!curr) {
            return;
        }
        inorder(curr->left);
        cout<<curr->data<<' ';
        inorder(curr->right);
    }
    void inorder() {
        inorder(head);
    }
    void preorder(node* curr) {
        if (!curr) return;
        cout<<curr->data<<' ';
        preorder(curr->left);
        preorder(curr->right);
    }
    void preorder() {
        preorder(head);
    }
    void postorder(node* curr) {
        if (!curr) return;
        postorder(curr->left);
        postorder(curr->right);
        cout<<curr->data<<' ';
    }
    void postorder() {
        postorder(head);
    }
    void del(node* &curr,int v) {
        if (!curr) return ;
        queue<node*>q;
        q.push(curr);
        node* key=nullptr;
        node* last=nullptr;
        node* parent=nullptr;

        while (!q.empty()) {
            node* temp=q.front();
            q.pop();
            last=temp;
            if (last->data==v) {
                key=last;
            }
            if (last->left) {
                parent=last;
                q.push(last->left);
            }
            if (last->right) {
                parent=last;
                q.push(last->right);
            }
        }
        if (key) {
            key->data=last->data;
            if (parent->left==last) {
                parent->left=nullptr;
            }
            else{
                parent->right=nullptr;
            }
            delete last;
        }

    }
    void del(int v) {
        del(head,v);
    }
};
int main() {
    LinkedList l;
    vector<int>arr;
    int n;
    cin>>n;
    for (int i=0;i<n;i++) {
        int v;
        cin>>v;
        arr.push_back(v);
    }
    l.insert(arr);
    l.inorder();
    cout<<'\n';
    l.preorder();
    cout<<'\n';
    l.postorder();
    cout<<'\n';
    l.del(3);
    l.inorder();

    return 0;
}
