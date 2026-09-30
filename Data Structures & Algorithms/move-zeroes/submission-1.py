class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
                        ## optimal approach
        w = 0
        i = 0
        ops_count = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[w] = nums[i]
                ops_count += 1
                w += 1

            i+= 1

        while w < len(nums):
            if nums[w] != 0:
                nums[w] = 0
                ops_count += 1

            w += 1
