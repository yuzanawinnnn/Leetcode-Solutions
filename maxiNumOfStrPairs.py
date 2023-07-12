class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(1,len(words)):
                if(i<j):
                    if(words[i] == words[j][::-1]):
                        count = count + 1
        return count
