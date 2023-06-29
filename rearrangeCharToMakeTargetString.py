class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = 0
        i = 0
        j = 0
        s = list(s)
        while target[j] in s:   
            if s[i] == target[j]:
                j = j + 1
                s[i] = " "
            i = i + 1
            if(j==len(target)):
                count = count + 1
                j = 0
            if(i==len(s)):
                i = 0
        return count

