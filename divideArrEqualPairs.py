class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = 0
        end = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i!=j and nums[i]==nums[j] and nums[i]!=""):
                    count = count + 1
                    nums[i] = ""
                    nums[j] = ""
        if(count == int(len(nums)/2)):
            return True
        else:
            return False

