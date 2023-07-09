class Solution:
    def sumBase(self, n: int, k: int) -> int:
        base_num = ""
        while n>0:
            dig = int(n%k)
            if dig<10:
                base_num = base_num+ str(dig)
            else:
                base_num = base_num + chr(ord('A')+dig-10)  #Using uppercase letters
            n = n // k
        base_num = base_num[::-1]
        return sum(list(map(int,list(base_num))))
