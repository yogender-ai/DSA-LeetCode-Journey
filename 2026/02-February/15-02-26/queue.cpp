/*
 * DSA Lesson · Queue
 *
 * Pattern : Data Structures & Algorithms
 * Written : 15 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
class queue{
    int* arr;
    int front;

    int capacity;
    int size;
public:
    queue(int cap){
        capacity=cap;
        arr=new int[cap];
        front=0;
        size=0;

    }
    void en(int val){
        if(size==capacity){
            cout<<"Overflow";
            return;
        }
        int rear=(front+size)%capacity;
        arr[rear]=val;
        size++;
    }
    void de(){
        if(size==0){
            cout<<"Underflow";
            return;
        }

        front=(front+1)%capacity;
        size--;
        return;

    }
    void gfront(){
        cout<<arr[front]<<endl;
        return;
    }
    void grear(){
        int rear=(front+size-1)%capacity;
        cout<<arr[rear]<<endl;
    }
};
int main(){
    queue q(5);
    q.en(9);
    q.en(8);
    q.en(7);
    q.gfront();
    q.grear();
    q.de();
    q.gfront();
    q.grear();

}
