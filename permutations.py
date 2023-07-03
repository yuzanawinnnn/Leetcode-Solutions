class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        arr = list(permutations(nums,len(nums)))
        return arr
