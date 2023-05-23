class Solution(object):
    def judgeCircle(self, moves):
        U = 0
        D = 0
        L = 0
        R = 0
        for i in moves:
            if i == "U":
                U = U +1
            elif i == "D":
                D = D +1
            elif i == "L":
                L = L +1
            elif i == "R":
                R = R +1
        if(U-D == 0 and L-R==0):
            return True
        else:
            return False
