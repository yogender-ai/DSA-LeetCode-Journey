/*
 * DSA Lesson · Trees
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
struct node {
    char data;
    node* sibling;
    node* fchild;
    node(int d) {
        data=d;
        sibling=nullptr;
        fchild=nullptr;
    }
};
class tree {
private:
    node* root;
public:
    tree() {
        root=nullptr;

    }
    void buildtree() {
        node* a=new node('a');
        node* b=new node('b');
        node* c=new node('c');
        node* d=new node('d');
        node* e=new node('e');
        node* f=new node('f');
        node* g=new node('g');
        node* h=new node('h');
        node* i=new node('i');
        node* j=new node('j');
        node* k=new node('k');
        node* l=new node('l');
        this->root=a;
        a->fchild=b;
        b->fchild=e;
        e->sibling=f;
        b->sibling=c;
        c->sibling=d;
        c->fchild=g;
        g->sibling=h;
        d->fchild=i;
        i->sibling=j;
        j->fchild=k;
        k->sibling=l;
    }
    void printtree() {
        cout<<"THis is my tree"<<" "<<"\n";
        preorder(this->root);
        cout<<endl;
    }

private:
    void preorder(node* n) {
        if (n==nullptr) {
            return;
        }
        cout<<n->data<<" ";
        preorder(n->fchild);
        preorder(n->sibling);
    }
};
int main() {
    tree mytreee;
    mytreee.buildtree();
    cout<<"You are great yogender you did it"<<endl;
    mytreee.printtree();
}
