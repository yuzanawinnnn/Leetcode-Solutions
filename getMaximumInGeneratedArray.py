class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if(n == 1):
            return 1
        if(n == 0):
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(1,n+1):
            if(2 * i >= 2 and 2 * i <= n):
                nums[2 * i] = nums[i]
            if(i * 2 + 1 >= 2 and i * 2 + 1 <= n):
                nums[2 * i + 1] = nums[i] + nums[i+1]
                
        return max(nums)
