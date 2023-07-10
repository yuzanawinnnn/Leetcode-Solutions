class Solution:
    def pivotInteger(self, n: int) -> int:
        num = list(map(int,range(1,n+1)))
        found = False
        i = 0
        while found == False and i<len(num):
            if(sum(num[:i+1]) == sum(num[i:])):
                found = True
                return num[i]
            i = i + 1
        return -1

            

