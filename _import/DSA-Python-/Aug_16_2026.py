# 347. Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1

        s = sorted(h.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for num in range(k):
            ans.append(s[num][0])
        return ans

# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        start = nums[0]
        temp = 1

        for i in range(1, len(nums)):
            if start + 1 == nums[i]:
                temp += 1
            elif start == nums[i]:
                continue
            else:
                temp = 1
            start = nums[i]
            if temp > count:
                count = temp

        return count

