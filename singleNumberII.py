class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        found = False
        i = 0
        while found == False and i<len(nums):
            if(nums.count(nums[i]) == 1):
                return nums[i]
                found = True
            i = i + 1
        if(found == False):
            return -1
