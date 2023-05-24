class Solution(object):
    def truncateSentence(self, s, k):
        ss = s.split(" ")
        res = ""
        for i in range(0,k):
            res = res + ss[i] + " "
        
        return res[:len(res)-1]
