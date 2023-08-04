class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        alpha = [x for x, x in enumerate(s) if x.isalpha() == True]
        alpha = alpha[::-1]
        j = 0
        for i in range(len(s)):
            if(s[i].isalpha() == True):
                s[i] = alpha[j]
                j = j + 1
        s = ''.join(s)
        return s

