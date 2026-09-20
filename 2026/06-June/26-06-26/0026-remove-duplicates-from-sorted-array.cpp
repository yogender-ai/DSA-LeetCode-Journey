/*
 * LeetCode 26 · Remove Duplicates from Sorted Array · Easy
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
using namespace std;
int main()
{
    int n=13;
    int arr[n]={1,3,3,2,3,4,4,4,5,5,5,5,5};
    int q=0;
    for (int i=0;i<n;i++)
    {
        for (int w=i+1;w<n;w++)
        {
            if (arr[w]==arr[i])


            {
                for (int j=w;j<n;j++)

                {
                    arr[j]=arr[j+1];


                }
                n=n-1;
                w--;
            }
        }

    }
    cout<<n<<"\n";
    for (int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
}
