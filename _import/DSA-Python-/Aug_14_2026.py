# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        left = 0
        right = len(nums) - 1
        q = sorted(nums)
        for i, num in enumerate(q):
            sum = q[left] + q[right]
            if sum == target:
                ind = nums.index(q[left])
                a.append(ind)
                nums[ind] = None

                a.append(nums.index(q[right]))
                break
            if sum > target:
                right -= 1
            else:
                left += 1
        return a

# 2. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
                return True
            else:
                count[num] = 1
        return False

#3.  Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w = list(t)
        for q in s:
            if q in w:
                ind = w.index(q)
                w.pop(ind)
            else:
                return False
        if not w:
            return True
        else:
            return False

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

