class Solution(object):
    def reverseWords(self, s):
        ss = ""
        s = s.split(" ")
        for i in range(len(s)):
            ss = ss + s[i][::-1] + " "
        
        return ss[:-1]
