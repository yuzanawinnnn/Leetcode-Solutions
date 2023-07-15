class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        count = 0
        total = 0
        while(numOnes > 0 and count<k):
            total = total + 1
            numOnes = numOnes - 1
            count = count + 1
        if(count<k):
            while(numZeros > 0 and count<k):
                numZeros = numZeros - 1
                count = count + 1
        if(count<k):
            while(numNegOnes > 0 and count<k):
                total = total - 1
                numNegOnes = numNegOnes - 1
                count = count + 1
        return total
