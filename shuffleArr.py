class Solution(object):
    def shuffle(self, nums, n):
        arr1 = nums[0:n]
        arr2 = nums[n:]
        arr =[]
        for i in range(len(arr1)):
            arr.append(arr1[i])
            arr.append(arr2[i])
        return arr
