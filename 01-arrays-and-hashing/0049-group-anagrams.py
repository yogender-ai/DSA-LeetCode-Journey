"""
LeetCode 49 · Group Anagrams · Medium
https://leetcode.com/problems/group-anagrams/

Pattern : Hash Map with sorted-string key
Solved  : 14 Aug 2026
Time    : O(n * k log k)  (approach 2)
Space   : O(n * k)
Note    : Approach 1 compares every pair -> O(n^2 * k log k) -> TLE.
"""
from typing import List

# Approach 1 — brute force (Time Limit Exceeded)
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


# Approach 2 — sorted word as key (Accepted)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in a:
                a[k] = []
            a[k].append(s)
        return list(a.values())
