class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        product = (nums[-1]-1)*(nums[-2]-1)

        return product
