/*
 * LeetCode 205 · Isomorphic Strings · Easy
 * https://leetcode.com/problems/isomorphic-strings/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    int b=123;
    string a=to_string(b);

    reverse(a.begin(),a.end());
    cout<<a;
}
