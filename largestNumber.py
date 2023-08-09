class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        found_duplicate = False
        i = 0
        nums.sort()
        arr = []
        while found_duplicate != True:
            if(nums.count(nums[i]) > 1):
                found_duplicate = True
                arr.append(nums[i])
            i = i + 1
        lost_found = False
        i = 0
        while lost_found != True:
            if(i+1 not in nums):
                arr.append(i+1)
                lost_found = True
            i = i + 1
        return arr
        

            
