class Solution(object):
    def buyChoco(self, prices, money):
        arr = []
        for i in range(len(prices)):
            for j in range(len(prices)):
                if(prices[i]+prices[j]<=money and i!=j):
                    arr.append(money-prices[i]-prices[j])
        if(len(arr) < 1):
            return money
        else:
            return max(arr)
