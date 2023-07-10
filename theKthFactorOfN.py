class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = [1]
        i = 2
        end = False
        while len(factor)<k and end==False:
            if(n%i == 0):
                factor.append(i)
            i = i + 1
            if(i>n):
                end = True
        if(end==True and k != len(factor)):
            return -1
        else:
            return factor[-1]

