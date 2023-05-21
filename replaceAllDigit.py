class Solution(object):
    def replaceDigits(self, s):
        alpha = list(map(chr, range(97, 123)))
        ss = ""
        for i in range(0,len(s)-1,2):
            print(s[i])
            ss = ss + s[i] + alpha[alpha.index(s[i])+int(s[i+1])]
        if(len(s) %2 != 0):
            ss = ss + s[-1]
        return ss
