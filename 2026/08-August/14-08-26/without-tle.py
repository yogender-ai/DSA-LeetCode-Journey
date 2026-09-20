"""
DSA Lesson · Without TLE

Pattern : Arrays & Hashing
Written : 14 Aug 2026
Time    : O(n)
Space   : O(1)
"""

# Without TLE
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in a:
                a[k] = []
            a[k].append(s)
        return list(a.values())
