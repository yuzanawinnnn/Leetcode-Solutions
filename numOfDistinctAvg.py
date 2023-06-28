class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()
        while len(nums) >0:
            nums.sort()
            avg.add((nums[0]+nums[-1])/2)
            nums.pop(-1)
            nums.pop(0)
        avg = list(avg)
        return len(avg)
