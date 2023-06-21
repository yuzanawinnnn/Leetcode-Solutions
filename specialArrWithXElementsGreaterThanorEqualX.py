class Solution:
    def specialArray(self, nums: List[int]) -> int:
        found = False
        j = 0
        while found == False and j<=max(nums):
            count = 0
            for i in range(len(nums)):
                if(nums[i] >= j):
                    count = count + 1
            if(count == j):
                found = True
            j = j + 1
        if(found == True):
            return count
        else:
            return -1


        

            
