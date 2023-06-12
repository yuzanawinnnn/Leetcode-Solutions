class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import Counter
        count= Counter(nums)
        max_count = count.most_common()[0][0]
        return max_count
        
