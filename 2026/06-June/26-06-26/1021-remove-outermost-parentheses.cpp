/*
 * LeetCode 1021 · Remove Outermost Parentheses · Easy
 * https://leetcode.com/problems/remove-outermost-parentheses/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

/*#include <iostream>
using namespace std;

string trim(string s) {
    int start = 0;
    int end = s.size() - 1;

    while (start <= end && s[start] == ' ') start++;
    while (end >= start && s[end] == ' ') end--;
    cout<<start<<"\n";
    cout<<end<<"\n";

    return s.substr(start, end-start+1 );
}

int main() {
    string s = "   hello world       ";
    cout << "[" << trim(s) << "]";
}*/
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;
int main()
{
    string num="52";
    int n=num.size();
    int arr[n];
    for (int i=0;i<n;i++){
        arr[i]=num[i]-'0';

    }
    int c;
    for(int i=0;i<n;i++){
        if(arr[i]%2!=0){
            c=arr[i];
        }
    }
    cout<< to_string(c);

}





