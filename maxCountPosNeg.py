class Solution(object):
    def maximumCount(self, nums):
        pos = neg = 0
        for i in range(len(nums)):
            if(nums[i]>0):
                pos = pos + 1
            elif(nums[i]<0):
                neg = neg + 1
        return max(pos,neg)
