class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        total = 0
        for i in range(len(n)):
            if(i%2==0):
                total = total + int(n[i])
            else:
                total = total - int(n[i])
        return total
