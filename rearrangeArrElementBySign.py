class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        j = 0
        k = 1
        for i in range(len(nums)):
            if(nums[i]>0):
                arr[j] = nums[i]
                j = j + 2
            else:
                arr[k] = nums[i]
                k = k + 2
        nums = arr
        return nums
                
