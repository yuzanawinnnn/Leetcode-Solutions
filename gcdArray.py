class Solution(object):
    def findGCD(self, nums):
        maxi = max(nums)
        mini = min(nums)
        found = False
        j = maxi
        while found == False and j>0:
            if(maxi%j == 0 and mini%j==0):
                found = True
                ans = j
            j = j-1
        return ans
