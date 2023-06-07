class Solution(object):
    def countElements(self, nums):
        nums.sort()
        count = 0
        for i in range(1,len(nums)-1):
            if(nums[0]<nums[i] and nums[len(nums)-1]>nums[i]):
                count = count +1
        return count
