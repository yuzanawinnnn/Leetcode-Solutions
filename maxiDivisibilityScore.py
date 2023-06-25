class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        scores = []
        maxi = 0
        for i in range(len(divisors)):
            count = 0
            for j in range(len(nums)):
                if(nums[j]%divisors[i] == 0):
                    count = count + 1
            if(count>maxi):
                maxi = count
                scores = [divisors[i]]
            elif(count == maxi):
                scores.append(divisors[i])
        scores.sort()
        return scores[0]
