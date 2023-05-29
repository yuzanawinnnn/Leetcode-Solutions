class Solution(object):
    def findMaxK(self, nums):
        arr = []
        for i in range(len(nums)):
            if((-1)*nums[i] in nums):
                arr.append(abs(nums[i]))
        if(len(arr)==0):
            return -1
        else:
            return max(arr)
