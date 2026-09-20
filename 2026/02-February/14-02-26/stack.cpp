/*
 * DSA Lesson · Stack
 *
 * Pattern : Data Structures & Algorithms
 * Written : 14 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
class node{
public:
    int data;

    node* next;
    node(int x){
        data=x;

        next=nullptr;
    }
};
class stack{
    node* head=nullptr;
public:
    void push(int x){
        node* newnode=new node(x);
        newnode->next=head;
        head=newnode;
    }
    int peek(){
        return head->data;
    }
    void pop(){
        node* temp=head;
        head=head->next;
        delete temp;
    }
};
int main(){
    stack s;
    s.push(6);
    s.push(5);
    cout<<s.peek()<<' ';
    s.pop();
    cout<<s.peek()<<' ';
}
