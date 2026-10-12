# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         currMax = nums[0]
#         globalMax = nums[0]

#         i = 1

#         while i < len(nums):
#             currMax = max(nums[i], currMax+nums[i])
#             globalMax = max(globalMax, currMax)

#             i += 1
        
#         return globalMax

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            maxi = max(sum, maxi)
            sum = 0 if sum < 0 else sum

        return maxi