class Solution(object):
    def sumOfUnique(self, nums):
        total = 0
        for i in range(len(nums)):
            if(nums.count(nums[i]) == 1):
                total = total + nums[i]
        return total
