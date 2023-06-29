class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        i = 0
        more3 = False
        while more3 == False and i<len(word1):
            if(abs(word1.count(word1[i])-word2.count(word1[i])) > 3):
                more3 = True
                return False
            if(abs(word2.count(word2[i])-word1.count(word2[i])) > 3):
                more3 = True
                return False
            i = i + 1
        if(more3 == False):
            return True
