class Solution(object):
    def arraySign(self, nums):
        ans = 1
        for i in range(len(nums)):
            ans = ans * nums[i]
        if(ans == 0):
            return 0
        elif(ans>0):
            return 1
        else:
            return -1
