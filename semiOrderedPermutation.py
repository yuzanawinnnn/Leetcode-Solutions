class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        swap = 0
        end = False
        while end == False:
            index_one = nums.index(1)
            while index_one != 0:
                temp = nums[index_one-1]
                nums[index_one-1] = 1
                nums[index_one] = temp
                swap = swap + 1
                index_one = nums.index(1)
            index_n = nums.index(len(nums))
            while index_n != len(nums)-1:
                temp = nums[index_n+1]
                nums[index_n+1] = len(nums)
                nums[index_n] = temp
                swap = swap + 1
                index_n = nums.index(len(nums))
            end = True
        return swap
