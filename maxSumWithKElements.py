class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        total = 0
        nums.sort()
        for i in range(k):
            total = total + nums[-1]
            nums.append(nums[-1]+1)
            nums.pop(len(nums)-2)
        return total
            
