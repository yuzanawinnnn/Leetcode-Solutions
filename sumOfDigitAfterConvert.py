class Solution(object):
    def getLucky(self, s, k):
        alpha = list(map(chr, range(97, 123)))
        ss = ""
        for i in range(len(s)):
            ss = ss + str(alpha.index(s[i])+1)
        print(ss)
    
        for j in range(k):
            total = 0
            for m in range(len(ss)):
                total = total + int(ss[m])
            ss = str(total)
            
        return total
        
            
            
