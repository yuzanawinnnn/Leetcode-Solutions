class Solution(object):
    def mostFrequent(self, nums, key):
        arr = {}
        for i in range(len(nums)):
            if(nums[i]==key and i+1<len(nums)):
                if(nums[i+1] not in arr.keys()):
                    arr[nums[i+1]] = 1
                else: 
                    arr[nums[i+1]] = arr[nums[i+1]] + 1
        for num, count in arr.items():  
            if count == max(arr.values()):
                return num
