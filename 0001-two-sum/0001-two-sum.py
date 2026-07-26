class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in d:
                return[i,d[needed]]  
            d[nums[i]] = i      