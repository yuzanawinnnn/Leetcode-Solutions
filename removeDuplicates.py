class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 0
        while nums[i] != "_" and i<len(nums)-1:
            if(nums.count(nums[i])>1):
                for j in range(nums.count(nums[i])-1):
                    nums.append("_")
                    nums.pop(i)
                    count = count + 1
            i = i + 1
        return len(nums)-count
