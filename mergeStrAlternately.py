class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        i = 0
        j = 0
        end = False
        while end == False:
            if(i < len(word1)):
                s = s + word1[i]
            if(j < len(word2)):
                s = s + word2[j]
            i = i + 1
            j = j + 1
            if(i>=len(word1) and j>=len(word2)):
                end = True
        return s
