class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        left_sum = 0
        right = [0]
        right_sum = 0
        arr = []
        for i in range(len(nums)-1):
            left_sum = left_sum + nums[i] 
            left.append(left_sum)
        for j in range(len(nums)-1,0,-1):
            right_sum = right_sum + nums[j]
            right.append(right_sum)
        right = right[::-1]
        for k in range(len(nums)):
            arr.append(abs(left[k]-right[k]))
        return arr

