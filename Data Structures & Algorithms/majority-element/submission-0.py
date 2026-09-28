class Solution:
    def majorityElement(self, nums):
        m = {}
        n = len(nums)
        for i in nums:
            if i in m.keys():
                m[i] += 1
            else:
                m[i] = 1
        
        maxEle = min(nums)

        for k,v in m.items():
            if v > n/2:
                maxEle = max(k, maxEle)
        
        return maxEle