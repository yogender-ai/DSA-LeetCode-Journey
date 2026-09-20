"""
LeetCode 4 · Median of Two Sorted Arrays · Hard
https://leetcode.com/problems/median-of-two-sorted-arrays/

Pattern : Binary Search
Solved  : 14 Aug 2026
Time    : O(n)
Space   : O(1)
"""

#4. Group Anagrams with TLE
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = list()
        for i in range(len(strs)):
            if strs[i] == None:
                continue
            temp = sorted(strs[i])

            l = list()
            l.append(strs[i])
            strs[i] = None
            for ii in range(i + 1, len(strs)):
                if strs[ii] == None:
                    continue
                tem = sorted(strs[ii])
                if tem == temp:
                    l.append(strs[ii])
                    strs[ii] = None

            ans.append(l)

        return ans
