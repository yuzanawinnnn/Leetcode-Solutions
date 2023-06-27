class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        text = text.split(" ")
        brokenLetters = list(brokenLetters)
        for i in range(len(text)):
            found = False
            j = 0
            while found == False and j<len(brokenLetters):
                if(brokenLetters[j] in text[i]):
                    found = True
                j = j + 1
            if(found == False):
                count = count + 1
        return count
