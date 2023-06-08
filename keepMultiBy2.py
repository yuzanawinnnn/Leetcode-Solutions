class Solution(object):
    def findFinalValue(self, nums, original):
        found = False
        num = original
        while found == False:
            if(num in nums):
                num = num * 2
            else:
                found = True
        return num
