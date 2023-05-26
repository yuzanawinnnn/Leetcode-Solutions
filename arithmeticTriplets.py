class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if(nums[i]-nums[j] == diff and nums[j]-nums[k] == diff and i!=j and j!=k and i!=k):
                        count = count +1
        return count
