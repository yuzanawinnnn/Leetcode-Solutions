class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        from itertools import combinations
        count = 0
        a = list(combinations(nums,2))
        for i in range(len(a)):
            if(abs(a[i][0]-a[i][1])==k):
                count = count + 1
        return count
            
