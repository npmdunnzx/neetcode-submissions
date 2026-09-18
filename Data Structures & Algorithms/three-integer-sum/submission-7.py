class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                tong = nums[i] + nums[left] + nums[right]
                if tong == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    if temp not in ans:
                        ans.append(temp)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif tong > 0:
                    right -= 1
                else:
                    left += 1
        return ans