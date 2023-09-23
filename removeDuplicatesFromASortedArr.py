class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_arr = list(set(nums))
        k = 0
        for i in range(len(unique_arr)):
            if(nums.count(unique_arr[i])>2):
                extra = nums.count(unique_arr[i]) - 2
                for j in range(extra):
                    nums.pop(nums.index(unique_arr[i]))
                    nums.append("_")
                    k = k + 1
        return len(nums)-k


        
