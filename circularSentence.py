class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(" ")
        i = 0
        while i<len(sentence)-1:
            if(sentence[i][-1] != sentence[i+1][0]):
                return False
            i = i + 1
        if(sentence[-1][-1] != sentence[0][0]):
            return False
        else:
            return True
