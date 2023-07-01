class Solution:
    def checkRecord(self, s: str) -> bool:
        substr = ""
        i = 0
        s = list(s)
        if(s.count('A')>=2):
            return False
        while len(substr)<3 and i<len(s):
            if(s[i]=='L'):
                substr = substr + "L"
            if(s[i]!='L'):
                substr= ""
            i = i + 1
        if len(substr)>=3:
            return False
        else:
            return True



