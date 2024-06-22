class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        temp = len(s) + 1
        while len(s)>0 and temp > len(s):
            temp = len(s)
            for i in range(1,len(s)):
                if(s[i] == ")" and s[i-1] == "(" or s[i] == "}" and s[i-1] == "{" or s[i] == "]" and s[i-1] == "["):
                    s.pop(i)
                    s.pop(i-1)
                    break
        if (len(s) == 0):
            return True
        else:
            return False
