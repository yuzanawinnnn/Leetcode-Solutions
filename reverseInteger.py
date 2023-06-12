class Solution(object):
    def reverse(self, x):
        string = str(abs(x))
        if(x<0):
            rev =  -1 * int(string[::-1])
            if(rev <= 2147483647 and rev>=-2147483648):
               return rev
            else:
                return 0
        else:
            rev = int(string[::-1])
            if(rev<= 2147483647 and rev>=-2147483648):
               return rev
            else:
                return 0
        
