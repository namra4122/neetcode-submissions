class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
                # # brute-force approach
        i = j = 0
        ops_count = 0

        for k in range(len(nums)):
            if nums[k] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
                ops_count += 2
            else:
                j += 1
