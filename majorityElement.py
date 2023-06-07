class Solution(object):
    def majorityElement(self, nums):
        maxi = 0
        nums.sort()
        arr = list(set(nums))
        for i in range(len(arr)):
            if(nums.count(arr[i]) > maxi):
                maxi = nums.count(arr[i])
                ans = arr[i]
                
        
        return ans
