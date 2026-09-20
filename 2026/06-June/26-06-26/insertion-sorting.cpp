/*
 * DSA Lesson · Insertion Sorting
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
    vector<int>nums={12,5,11,4,16};
    int n=nums.size();
    cout<<"Now we are going to sort this array by Insertion sort"<<"\n";
    for (int i=1;i<n;i++)
    {
        int key=nums[i];
        int j=i-1;
        while (j>=0&&nums[j]>key)
        {
            nums[j+1]=nums[j];
            j--;
        }
        nums[j+1]=key;
    }
    for (int i=0;i<n;i++)
    {
        cout<<nums[i]<<" ";
    }
}
