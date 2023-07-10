class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            s = str(nums[i])
            nums.append(int(s[::-1]))
        nums = set(nums)
        return len(nums)
