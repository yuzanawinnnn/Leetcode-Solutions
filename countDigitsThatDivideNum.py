class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        count = 0
        for i in range(len(s)):
            if(num%int(s[i])==0):
                count = count + 1
        return count
