class Solution(object):
    def repeatedNTimes(self, nums):
        found = False
        i = 0
        while found == False:
            if(nums.count(nums[i]) == int(len(nums)/2)):
                ans = nums[i]
                found = True
            i = i +1
        return ans
            
