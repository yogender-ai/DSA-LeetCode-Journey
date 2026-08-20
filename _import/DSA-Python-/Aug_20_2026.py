# 15. 3Sum
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        a = 0
        nums.sort()
        for a in range(len(nums) - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            left = a + 1
            right = len(nums) - 1
            if nums[a] > 0:
                break

            while left < right:
                sum = nums[left] + nums[right] + nums[a]
                if sum == 0:
                    temp = [nums[left], nums[right], nums[a]]
                    ans.append(temp)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # skip duplicates on right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum > 0:
                    right -= 1
                else:
                    left += 1

        return ans

