class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        arr = []
        i = 0
        while i<len(nums):
            end = False
            j = i
            s=""
            while end == False and j<len(nums):
                if(nums[j]==1):
                    s = s + '1'
                else:
                    end = True
                j = j + 1
            i = j
            arr.append(len(s))
        return max(arr)

