class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        temp1 = []
        temp2 = []
        if(len(s) != len(pattern)):
            return False
        for i in range(len(s)):
            if(s[i] not in temp1 and pattern[i] not in temp2):
                temp1.append(s[i])
                temp2.append(pattern[i])
            elif(s[i] in temp1 and temp2[temp1.index(s[i])] == pattern[i]):
                continue
            else:
                return False
        return True


        
