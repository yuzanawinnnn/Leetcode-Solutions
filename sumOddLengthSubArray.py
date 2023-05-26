class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                temp = arr[i:j+1]
                if(len(temp)%2 != 0):
                    print(temp)
                    total = total + sum(temp)
        return total
