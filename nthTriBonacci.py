class Solution:
    def tribonacci(self, n: int) -> int:
        Tri = [0,1,1]
        if(n<3):
            return Tri[n]
        for i in range(3,n+1):
            Tri.append(Tri[-1]+Tri[-2]+Tri[-3])
        return Tri[-1]
