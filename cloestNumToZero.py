class Solution(object):
    def findClosestNumber(self, nums):
        num = []
        for i in range(len(nums)):
            num.append(abs(nums[i]))
        if(num.count(min(num))>1):
            maxi = min(nums)
            for j in range(len(num)):
                if(num[j] == min(num)):
                    if(nums[j]>maxi):
                        maxi = nums[j]
        else:
            maxi = nums[num.index(min(num))]
        return maxi
