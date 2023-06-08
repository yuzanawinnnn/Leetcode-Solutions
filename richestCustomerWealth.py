class Solution(object):
    def maximumWealth(self, accounts):
        arr = []
        for i in range(len(accounts)):
            arr.append(sum(accounts[i]))
        return max(arr)
