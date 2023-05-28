class Solution(object):
    def uniqueOccurrences(self, arr):
        arr1 = {}
        for i in range(len(arr)):
            arr1[arr[i]] = arr.count(arr[i])
        arr2 = set(arr1.values())
        if(len(arr2) != len(arr1)):
            return False
        else:
            return True
