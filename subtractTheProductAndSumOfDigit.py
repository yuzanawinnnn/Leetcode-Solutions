class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int,list(str(n))))
        prod = 1
        total = 0
        for i in range(len(n)):
            prod = prod * n[i]
            total = total + n[i]
        return prod - total
