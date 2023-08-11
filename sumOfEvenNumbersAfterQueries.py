class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        total = sum(n for n in nums if not n%2)
        for i in range(len(queries)):
            if(nums[queries[i][1]] % 2 == 0):
                total = total - nums[queries[i][1]]
            nums[queries[i][1]] = nums[queries[i][1]] + queries[i][0]
            if(nums[queries[i][1]] % 2 == 0):
                total = total + nums[queries[i][1]]
            answer.append(total)
        return answer

            
