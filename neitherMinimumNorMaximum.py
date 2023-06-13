class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if(len(nums)<3):
            return -1
        else:
            maxi = max(nums)
            mini = min(nums)
            found = False
            i = 0
            while found != True and i<len(nums):
                if(nums[i] != maxi and nums[i]!=mini):
                    found = True
                    ans = nums[i]
                i = i + 1
            return ans
