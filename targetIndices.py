class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        arr = []
        for i in range(len(nums)):
            if(nums[i] == target):
                arr.append(i)
        return arr
            
