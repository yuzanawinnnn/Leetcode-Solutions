class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        temp = ""
        for i in range(len(words)):
            temp = temp + list(words[i])[0]
        if(temp == s):
            return True
        else:
            return False
