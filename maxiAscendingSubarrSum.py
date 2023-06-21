class Solution:
    def maxAscendingSum(self, nums):
        if(len(nums)==1):
            return nums[0]
        arr = []
        i = 0
        while i<len(nums)-1:
            j = i + 1
            total = nums[i]
            while nums[j-1]<nums[j] and j<len(nums)-1:
                total = total + nums[j]
                j = j + 1
            if(nums[j]>nums[j-1]):
                total = total + nums[j]
            arr.append(total)
            i = j
        if(len(arr)==1):
            return arr[0]
        else:
            return max(arr)
