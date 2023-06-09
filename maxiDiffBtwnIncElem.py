class Solution(object):
    def maximumDifference(self, nums):
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i!=j and i<j and nums[j]>nums[i]):
                    arr.append(nums[j]-nums[i])
        if(len(arr)==0):
            return -1
        else:
            return max(arr)
