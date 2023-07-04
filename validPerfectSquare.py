class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        n = str(math.sqrt(num))
        if(len(n[n.index('.')+1:])== 1 and n[-1]=='0'):
            return True
        else:
            return False
