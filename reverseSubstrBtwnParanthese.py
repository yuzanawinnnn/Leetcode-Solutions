class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        i = 0
        while i<len(s):
            if(s[i]==")"):
                index = i-1
                temp = ""
                while s[index] !="(":
                    temp = temp + s[index]
                    index = index - 1
                s = s[:index] + list(temp)+s[i+1:]
                i = i - 2
            i = i + 1
        s = ''.join(s)
        return s                

                
