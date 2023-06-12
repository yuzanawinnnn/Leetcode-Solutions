class Solution:
    def moveZeroes(self, nums): 
        i = 0
        j = 0
        while i<len(nums):
            if(nums[j] == 0):
                nums.pop(j)
                nums.append(0)
            if(nums[j] != 0):
                j = j + 1
            i = i + 1

        
