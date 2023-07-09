class Solution:
    def isThree(self, n: int) -> bool:
        count = 1
        i = 2
        end = False
        while end == False:
            if(n%i==0):
                count = count + 1
            i = i + 1
            if(count>3 or i>n):
                end = True
        if(count==3):
            return True
        else:
            return False
