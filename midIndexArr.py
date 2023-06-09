class Solution(object):
    def findMiddleIndex(self, nums):
        found = False
        i = 0
        while found == False and i<len(nums):
            substr1 = nums[:i]
            result1 = sum(substr1)
            if(i==len(nums)-1):
                result2 = 0
            else:
                substr2 = nums[i+1:]
                result2 = sum(substr2)
            if(result1 == result2):
                found = True
                mid_index = i
            i = i + 1
        if(found == False):
            return -1
        else:
            return mid_index
                
            
