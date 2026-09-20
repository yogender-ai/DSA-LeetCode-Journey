/*
 * DSA Lesson · Stack
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

/*#include <iostream>
using namespace std;
struct node
{
     int data;
     node* prev;
     node* next;
     node(int d)
     {
          data=d;
          prev=nullptr;
          next=nullptr;
     }
};
class queue
{
private:
     node* head;
     node* tail;
public:
     queue()
     {
          head=nullptr;
          tail=nullptr;
     }
     void pushinq(int data)

     {
          node* newnode=new node(data);
          if (head==nullptr)
          {
               head=newnode;
               tail=newnode;
          }
          else
          {
               tail->next = newnode;
               newnode->prev = tail;
               tail = newnode;
          }

     }
     void display()
     {
          node* temp=head;
          while (temp!=nullptr)
          {
               cout<<temp->data<<" ";
               temp=temp->next;

          }
     }
     void delinq()
     {
          node* temp=head;
          head=temp->next;
          delete temp;
     }

};
int main()
{
     queue q;
     q.pushinq(5);
     q.pushinq(6);
     q.pushinq(7);
     q.pushinq(8);
     q.display();
     q.delinq();
     q.delinq();
     cout<<"\n";
     q.display();


}*/
