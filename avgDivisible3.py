class Solution(object):
    def averageValue(self, nums):
        total = 0
        count = 0
        for i in range(len(nums)):
            if(nums[i]%3 ==0 and nums[i]%2==0):
                total = total + nums[i]
                count = count + 1
        if(count == 0):
            return 0
        else:
            return int(total/count)
