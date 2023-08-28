class Solution:
    def finalString(self, s: str) -> str:
        temp = []
        s = list(s)
        for i in range(len(s)):
            if(s[i] != "i"):
                temp.append(s[i])
            else:
                temp = temp[::-1]
        temp = ''.join(temp)
        return temp
