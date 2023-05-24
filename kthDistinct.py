class Solution(object):
    def kthDistinct(self, arr, k):
        count = 0
        temp = ""
        for i in range(len(arr)):
            if(arr.count(arr[i]) == 1):
                count = count +1
                if(count == k):
                    temp = arr[i]
        return temp
