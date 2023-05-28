class Solution(object):
    def smallestEqual(self, nums):
        flag = False
        i = 0
        while flag == False and i < len(nums):
            if(nums[i] == i%10):
                flag = True
                return i
            i = i + 1
        if(flag == False):
            return -1
