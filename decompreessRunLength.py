class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        arr = []
        while i < len(nums):
            substr = nums[i:i+2]
            for j in range(substr[0]):
                arr.append(substr[1])
            i = i + 2
        return arr
