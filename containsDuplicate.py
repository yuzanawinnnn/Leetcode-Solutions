class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_arr = list(set(nums))
        if(len(nums) == len(distinct_arr)):
            return False
        else:
            return True
