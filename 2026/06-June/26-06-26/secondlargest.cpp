/*
 * DSA Lesson · Secondlargest
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include<iostream>
using namespace std;
int main()
{
    int arr[6]={16,13,8,9,12,20};
    int large;
    int second;
    int third;
    large=arr[0];
    second=arr[1];
    if (second>large)
    {
        swap(arr[1],arr[0]);
    }
    int temp;
    for (int i=2;i<6;i++)
    {
        if (arr[i]>second && arr[i]>large)
        {
            temp=large;
            large=arr[i];
            second=temp;


        }

    }
    cout<<large<<"\n";
    cout<<second;

}
