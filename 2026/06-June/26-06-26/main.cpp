/*
 * DSA Lesson · Main
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
#include "bst.h"
using namespace std;
int main(){
    bst tree;
    tree.insert(5);
    tree.insert(6);
    tree.insert(10);
    tree.insert(2);
    tree.insert(1);
    tree.insert(3);
    tree.inorder();
    tree.deletion(5);
    cout<<"After Delete\n";
    tree.inorder();
}
