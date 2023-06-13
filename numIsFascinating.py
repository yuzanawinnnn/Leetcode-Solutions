class Solution:
    def isFascinating(self, n: int) -> bool:
        s = str(n)+str(2*n)+str(3*n)
        i = 1
        found = False
        while found != True and i<=len(s):
            if(str(i) not in s):
                found = True
            i = i + 1
        if(found == False):
            return True
        else:
            return False
