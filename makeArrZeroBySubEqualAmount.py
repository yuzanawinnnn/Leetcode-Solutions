class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        import numpy as np
        count = 0
        nums = np.array(nums)
        while sum(nums) != 0: 
            minval = np.min(nums[np.nonzero(nums)])
            for i in range(len(nums)):
                if(nums[i]!=0):
                    nums[i] = nums[i]- minval
            count = count + 1
        return count
