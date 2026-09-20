/*
 * DSA Lesson · Bubblesort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int>array={1,2,3,4,5};
    cout<<"In this we are using Bubble sort.";
    int n= array.size();
    for (int i=n-1;i>=0;i--)
    {
        for (int j=0;j<n;j++)
        {
            if (array[j]>array[j+1])
            {
                swap(array[j],array[j+1]);
            }
        }
    }
    cout<<"This is your sorted array"<<"\n";
    for (int i=0;i<n;i++)
    {
        cout<<array[i]<<" ";
    }
}
