class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        found = False
        i = 0
        while found == False and i<len(nums):
            if(sum(nums[:i]) == sum(nums[i+1:])):
                found = True   
                index = i 
            i = i + 1
        if(found == False):
            return -1
        else:
            return index
