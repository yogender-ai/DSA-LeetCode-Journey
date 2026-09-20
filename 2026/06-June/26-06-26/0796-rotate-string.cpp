/*
 * LeetCode 796 · Rotate String · Easy
 * https://leetcode.com/problems/rotate-string/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
    string goal="abdce";
    int m=goal.size();
    vector<int> arr(m);
    int temp;
    for(int i=0;i<m;i++){
        temp=int(goal[i]);
        arr[i]=temp;
    }

    int y;
    for (int i=0;i<m;i++)
    {
        if(i==m-1 && arr[i]<arr[i+1]){
            y=1;
        }
        else if(arr[i]<arr[i+1]){
            y=1;
        }
        else{
            y=0;
            break;
        }
    }
    cout<<y;
}
