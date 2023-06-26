class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 0
        while i<len(words):
            j = 1
            while j<len(words):
                if(i == j-1 and sorted(words[i]) == sorted(words[j])):
                    words.pop(j)
                else:
                    j = j + 1
            i = i + 1
        return words
