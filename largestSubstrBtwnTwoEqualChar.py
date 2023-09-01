class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxi = -1
        s = list(s)
        reverse = s[::-1]
        for i in range(len(s)):
            if(s.count(s[i]) > 1):
                maxi = max(len(s) - reverse.index(s[i]) -2 - i, maxi)
        return maxi
                

                
        
