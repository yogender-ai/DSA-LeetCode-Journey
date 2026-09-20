/*
 * DSA Lesson · Selectionsorting
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
   vector<int>array={30,1,40,23,56};
    cout<<"These are element of array"<<"\n";
    int n=array.size();
    for (int i=0;i<n;i++)
    {
        cout<<array[i]<<" ";
    }
    cout<<"\n"<<"1 for ascending and 2 for descending"<<"\n";
    int choice;
    cin>>choice;
    if (choice==1)
    {
        for (int i=0;i<n-1;i++)
        {
            int min=i;
            for (int j=i+1;j<n;j++)
            {
                if (array[j]<array[min])
                {
                    min=j;
                }
            }
            swap(array[i],array[min]);
        }

        cout<<"This is your ascending array Thank you!"<<"\n";
        for (int i=0;i<n;i++)
        {
            cout<<array[i]<<" ";
        }
    }
    else
    {
        for (int i=0;i<n-1;i++)
        {
            int big=i;
            for (int j=i+1;j<n;j++)
            {
                if (array[j]>array[big])
                {
                    big=j;
                }

            }
        swap(array[i],array[big]);
        }
            cout<<"This is your descending array Thank you!"<<"\n";
        for (int i=0;i<n;i++)
        {
            cout<<array[i]<<" ";
        }
    }

}
