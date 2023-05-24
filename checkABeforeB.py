class Solution(object):
    def checkString(self, s):
        if("b" in s):
            index = s.index("b")
            sub = s[index:]
        else:
            sub = ""
        if 'a' in sub:
            return False
        else:
            return True
        
