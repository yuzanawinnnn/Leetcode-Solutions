class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr =[]
        for i in range(len(nums)):
            total = 0
            for j in range(len(nums)):
                if(nums[i] > nums[j] and i != j):
                    total = total +1
            arr.append(total)
        return arr
