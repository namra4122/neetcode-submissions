class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[w]:
                w += 1
                nums[w] = nums[i]

        return w+1