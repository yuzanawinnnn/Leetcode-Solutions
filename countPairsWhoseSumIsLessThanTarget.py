class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        done = []
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(i<j and nums[i]+nums[j]<target):
                    count = count + 1
        return count
