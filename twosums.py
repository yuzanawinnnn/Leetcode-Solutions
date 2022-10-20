from typing import List
class Solution:
    def twoSum(self, nums, target):
        values = {}
        for i, j in enumerate(nums):
            if (target - j in values):
                return [values[target - j], i]
            else:
                values[j] = i
        
