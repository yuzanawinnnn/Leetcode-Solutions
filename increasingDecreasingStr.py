class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        s.sort()
        ss = s[0]
        inc = True
        dec = False
        s.pop(0)
        while len(s) > 0:
            if(inc == True):
                found = False
                i = 0
                while found != True and i<len(s):
                    if(s[i]>ss[-1]):
                        ss = ss + s[i]
                        s.pop(i)
                        found = True
                    else:
                        i = i + 1
                if(found == False):
                    inc = False
                    dec = True
                    s = s[::-1]
                    ss = ss + s[0]
                    s.pop(0)
            else:
                flag = False
                j = 0
                while flag != True and j<len(s):
                    if(s[j]<ss[-1]):
                        ss = ss + s[j]
                        s.pop(j)
                        flag = True
                    else:
                        j = j + 1
                if(flag == False):
                    inc = True
                    dec = False
                    s.sort()
                    ss = ss + s[0]
                    s.pop(0)
        return ss
                

            

            
