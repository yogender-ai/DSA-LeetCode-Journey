/*
 * LeetCode 728 · Self Dividing Numbers · Easy
 * https://leetcode.com/problems/self-dividing-numbers/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int w=n;
    while(n!=0){
        int q=n%10;
        n=n/10;
        if(w%q==0){
            continue;
        }
        else{
            false;
            break;
        }
    }
    cout<<true;
}
