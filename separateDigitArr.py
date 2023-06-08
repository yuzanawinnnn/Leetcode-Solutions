class Solution(object):
    def separateDigits(self, nums):
        arr = []
        for i in range(len(nums)):
            for j in range(len(str(nums[i]))):
                arr.append(int(str(nums[i])[j]))
        return arr
