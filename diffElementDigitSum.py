class Solution(object):
    def differenceOfSum(self, nums):
        element = 0
        digit = 0
        for i in range(len(nums)):
            element = element + nums[i]
            if(nums[i]<10):
                digit = digit + nums[i]
            elif(nums[i]>=10):
                temp = str(nums[i])
                for j in temp:
                    digit = digit + int(j)
               
        result = abs(element - digit)
        return result
