class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        while nums.count(val)!=0:
            nums.pop(nums.index(val))
            nums.append('_')
            count = count + 1    
        
        return len(nums)-count
        
