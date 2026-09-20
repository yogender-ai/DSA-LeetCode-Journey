/*
 * DSA Lesson · Creation
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

class Node {
public:
    int data;
    Node* next;

    Node(int d) : data(d), next(nullptr) {}
};

// ------------------ Create List ------------------
Node* createList(const vector<int>& arr) {
    Node* head = new Node(arr[0]);
    Node* curr = head;

    for(int i = 1; i < arr.size(); i++) {
        curr->next = new Node(arr[i]);
        curr = curr->next;
    }
    return head;
}

// ------------------ Print List ------------------
void printList(Node* head) {
    while(head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

// ------------------ Length ------------------
int length(Node* head) {
    int cnt = 0;
    while(head) {
        cnt++;
        head = head->next;
    }
    return cnt;
}

// ------------------ Delete Nth From End ------------------
Node* deleteNthFromEnd(Node* head, int n) {
    int len = length(head);
    int pos = len - n;

    if(pos == 0) {
        Node* temp = head;
        head = head->next;
        delete temp;
        return head;
    }

    Node* curr = head;
    for(int i = 1; i < pos; i++)
        curr = curr->next;

    Node* del = curr->next;
    curr->next = del->next;
    delete del;

    return head;
}

// ------------------ Reverse List ------------------
Node* reverseList(Node* head) {
    Node* prev = nullptr;
    Node* curr = head;

    while(curr) {
        Node* nextNode = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    return prev;
}

// ------------------ Insert At Front ------------------
Node* insertFront(Node* head, int x) {
    Node* temp = new Node(x);
    temp->next = head;
    return temp;
}

// ------------------ Print Alternate ------------------
void printAlternate(Node* head) {
    int idx = 0;
    while(head) {
        if(idx % 2 == 0)
            cout << head->data << " ";
        idx++;
        head = head->next;
    }
    cout << endl;
}

// ------------------ Print From Middle ------------------
void printFromMiddle(Node* head) {
    int len = length(head);
    int mid = len / 2;

    for(int i = 0; i < mid; i++)
        head = head->next;

    while(head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}

// ------------------ MAIN ------------------
int main() {
    vector<int> arr = {2, 5, 6, 10, 13};

    Node* head = createList(arr);

    cout << "Original List: ";
    printList(head);

    cout << "Length: " << length(head) << endl;

    head = deleteNthFromEnd(head, 2);
    cout << "After Deleting 2nd from End: ";
    printList(head);

    cout << "Alternate Nodes: ";
    printAlternate(head);

    head = reverseList(head);
    cout << "Reversed List: ";
    printList(head);

    head = insertFront(head, 1);
    cout << "After Inserting 1 at Front: ";
    printList(head);

    cout << "From Middle: ";
    printFromMiddle(head);
}
