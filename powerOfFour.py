class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        i = 0
        found = False
        while math.pow(4,i)<=n and found == False:
            if(int(math.pow(4,i))==n):
                found = True
                return True
            i = i + 1
        if(found == False):
            return False
