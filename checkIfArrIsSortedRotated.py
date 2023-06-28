class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_arr = sorted(nums)
        end = False
        i = 0
        while end == False and i<nums.count(sorted_arr[0]):
            start = [j for j, n in enumerate(nums) if n == sorted_arr[0]][i]
            rotated_arr = nums[start:] + nums[:start]
            if(rotated_arr == sorted_arr):
                end = True
                return True
            else:
                i = i + 1
        if(end==False):
            return False
