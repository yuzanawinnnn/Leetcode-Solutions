class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        arr = []
        for i in range(len(nums)):
            if(nums[i] == target):
                arr.append(abs(i-start))
        arr.sort()
        return arr[0]
