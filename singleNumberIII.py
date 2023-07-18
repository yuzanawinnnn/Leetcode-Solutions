class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if(nums.count(nums[i])==1):
                answer.append(nums[i])
        return answer
