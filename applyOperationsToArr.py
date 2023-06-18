class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr = []
        zero = []
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        if(nums[len(nums)-2]==nums[len(nums)-1]):
            nums[len(nums)-2] = nums[len(nums)-2] * 2
            nums[len(nums)-1] = 0
        for k in range(len(nums)):
            if(nums[k]==0):
                zero.append(0)
            else:
                arr.append(nums[k])
        arr = arr + zero
        return arr
