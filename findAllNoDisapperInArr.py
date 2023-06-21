class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        number = list(map(int,range(1,len(nums)+1)))
        ans = list(set(nums) ^ set(number))
        return ans
