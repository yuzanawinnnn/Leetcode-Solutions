class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero = 0
        one = 0
        count_zero = 0
        count_one = 0
        s = list(map(int,list(s)))
        if(s[0] == 1):
            count_one = 1
        else:
            count_zero = 1
        for i in range(1,len(s)):
            if(s[i] == s[i-1]):
                if(s[i]==1):
                    count_one = count_one + 1
                    count_zero = 0
                else:
                    count_zero = count_zero + 1
                    count_one = 0
            else:
                if(count_one != 0):
                    one = max(one,count_one)
                    count_one = 0
                    count_zero = 1
                else:
                    zero = max(zero, count_zero)
                    count_zero = 0
                    count_one = 1
        one = max(one,count_one)
        zero = max(zero,count_zero)
        if(one > zero):
            return True
        else:
            return False



