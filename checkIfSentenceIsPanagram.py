class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = list(set(list(sentence)))
        if(len(sentence)==26):
            return True
        else:
            return False
