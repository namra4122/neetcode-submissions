class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        globalMax = nums[0]

        i = 1

        while i < len(nums):
            currMax = max(nums[i], currMax+nums[i])
            globalMax = max(globalMax, currMax)

            i += 1
        
        return globalMax