class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue

            temp = currMax * n
            currMax = max(n, temp, currMin*n)
            currMin = min(n, temp, currMin*n)
            res = max(res, currMax)

        return res