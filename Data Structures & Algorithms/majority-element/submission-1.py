from collections import Counter

class Solution:
    def majorityElement(self, nums):
        return next(x for x, count in Counter(nums).items() if 2*count  > len(nums))