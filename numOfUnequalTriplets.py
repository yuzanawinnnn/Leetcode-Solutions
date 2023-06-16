class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        from itertools import combinations
        count = 0
        arr = list(combinations(nums,3))
        for i in range(len(arr)):
            if(arr[i][0] != arr[i][1] and arr[i][1] != arr[i][2] and arr[i][0] != arr[i][2]):
                count = count + 1
        return count
