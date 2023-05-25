class Solution(object):
    def runningSum(self, nums):
        arr = []
        arr.append(nums[0])
        for i in range(1,len(nums)):
            total = 0
            for j in range(i+1):
                total = total + nums[j]
            arr.append(total)
        return arr
