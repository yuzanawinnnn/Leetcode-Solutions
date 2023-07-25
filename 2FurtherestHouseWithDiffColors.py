class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxi = 0
        for i in range(len(colors)):
            for j in range(1,len(colors)):
                if(colors[i]!=colors[j]):
                    maxi = max(abs(i-j),maxi)
        return maxi
