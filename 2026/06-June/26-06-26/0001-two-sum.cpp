/*
 * LeetCode 1 · Two Sum · Easy
 * https://leetcode.com/problems/two-sum/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

// ==========================================================
//  CodeShelf — LeetCode Solution
// ==========================================================
//  Problem:    Two Sum
//  URL:        https://leetcode.com/problems/two-sum/
//  Difficulty: Medium
//  Tags:       Array, Hash Table
//  Approach:  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//             
//             You may assume that each input would have exactly one solution, and you may not use the same element twice.
//             
//             You can return the answer in any order.
//             
//             
//             Example 1:
//             
//             Input: nums = [2,7,11,15], target = 9
//             Output: [0,1]
//             Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
//             
//             
//             Example 2:
//             
//             Input: nums = [3,2,4], target = 6
//             Output: [1,2]
//             
//             
//             Example 3:
//             
//             Input: nums = [3,3], target = 6
//             Output: [0,1]
//             
//             
//             
//             Constraints:
//             
//             
//             2 <= nums.length <= 104
//             -109 <= nums[i] <= 109
//             -109 <= target <= 109
//             Only one valid answer exists.
//             
//             
//             
//             Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
// ==========================================================
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size()-1;
        vector<int>ans;
        vector<int>nums1=nums;
        sort(nums.begin(),nums.end());
        while(left<right){
           
            if(nums[left]+nums[right]==target){
                ans.push_back(left);
                ans.push_back(right);
                break;
            }
            else if(nums[left]+nums[right]>target){
                right--;

            }
            else{
                left++;
            }
        }
        vector<int>q;
        if(!ans.empty()){
            for(int a:ans){
                int w=nums[a];
                auto it=find(nums1.begin(),nums1.end(),w);
                if(it!=nums1.end()){
                    q.push_back(it-nums1.begin());
                    nums1[it-nums1.begin()]= -1;
                }
            }
        }
        return q;
    }
};
