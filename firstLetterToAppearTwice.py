class Solution:
    def repeatedCharacter(self, s: str) -> str:
        i = 0 
        s = list(s)
        found = False
        mini_index = len(s)
        letter =""
        while i<len(s):
            if(s.count(s[i])>1):
                index = s[s.index(s[i])+1:].index(s[i])+ s.index(s[i])
                if(index<mini_index):
                    mini_index = index
                    letter = s[i]
            i = i + 1
        return letter
