/*
 * DSA Lesson · Quick Sort
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for (int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    int pi;
    pi=arr[n-1];
    int k=0;
    for (int i=0;i<n;i++)
    {
        if (arr[n-1]>arr[i])
        {
            arr[k]=arr[i];
            k++;
        }

    }
    int q=1;
    arr[k]=pi;
    for (int i=0;i<n;i++)
    {
        if (arr[k]<arr[i])
        {
            arr[k+q]=arr[i];
            q++;
        }
    }
    for (int i=0;i<n;i++)
    {
        cout<<" "<<arr[i];
    }
}#include <iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for (int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    int pi;
    pi=arr[n-1];
    int k=0;
    for (int i=0;i<n;i++)
    {
        if (arr[n-1]>arr[i])
        {
            arr[k]=arr[i];
            k++;
        }

    }
    int q=1;
    arr[k]=pi;
    for (int i=0;i<n;i++)
    {
        if (arr[k]<arr[i])
        {
            arr[k+q]=arr[i];
            q++;
        }
    }
    for (int i=0;i<n;i++)
    {
        cout<<" "<<arr[i];
    }
}
