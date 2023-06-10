class Solution(object):
    def dominantIndex(self, nums):
        i = 0
        found = False
        maxi = max(nums)
        index = nums.index(maxi)
        while i<len(nums) and found == False:
            if(i != index):
                if( 2 * nums[i] > maxi):
                    found = True
            i = i + 1
        if(found == True):
            return -1
        else:
            return index
