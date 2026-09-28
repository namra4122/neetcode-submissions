class Solution:
    def majorityElement(self, nums):
        # boyer-moore voting Solution
        x = -100000
        count = 0

        # find potential ans
        for n in nums:
            if count == 0:
                x = n
            
            count += 1 if n == x else -1
        
        v = 0
        for i in nums:
            if i == x:
                v += 1
        
        return x if v > len(nums)//2 else -1