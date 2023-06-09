class Solution(object):
    def mostFrequentEven(self, nums):
        from collections import Counter
        arr = []
        for i in range(len(nums)):
            if(nums[i]%2==0): 
                arr.append(nums[i])
        if(len(arr)==0):
            return -1
        else:
            count= Counter(arr)
            max_count = count.most_common()[0][1]
            mini = max(arr)
            for j in range(len(arr)):
                if(arr.count(arr[j])==max_count and mini>arr[j]):
                    mini = arr[j]
            return mini
        
