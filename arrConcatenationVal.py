class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        total = 0
        while len(nums)>0:
            if(len(nums)>1):
                total = total + int(str(nums[0])+str(nums[-1]))
                nums.pop(len(nums)-1)
                nums.pop(0)
            else:
                total = total + nums[0]
                nums.pop(0)
        return total

            
