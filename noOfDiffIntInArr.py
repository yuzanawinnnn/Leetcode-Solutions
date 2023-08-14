class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        import re
        word = re.sub(r'[a-zA-z]','/',word)
        word = list(set(word.split("/")))
        count = 0
        i = 0
        while i<len(word):
            if(word[i] != ""):
                i = i + 1
            else:
                word.pop(i)
        word = list(set(list(map(int,word))))
        return len(word)
