class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        i = 2
        found = False
        while found == False and i<=n-2:
            base_num = ""
            num = n
            while num>0:
                dig = int(num%i)
                if dig<10:
                    base_num = base_num+ str(dig)
                else:
                    base_num = base_num + chr(ord('A')+dig-10) 
                num = num // i
            if(base_num != base_num[::-1]):
                found = True
                return False
            else:
                i = i + 1
        return True
