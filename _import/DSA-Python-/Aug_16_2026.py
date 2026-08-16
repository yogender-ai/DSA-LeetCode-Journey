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
