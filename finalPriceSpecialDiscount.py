class Solution(object):
    def finalPrices(self, prices):
        arr = []
        for i in range(len(prices)):
            found = False
            j = i + 1
            while found == False and j<len(prices):
                if(prices[i]>=prices[j]):
                    arr.append(prices[i] - prices[j])
                    found = True
                j = j + 1
            if(found == False):
                arr.append(prices[i])
        return arr
