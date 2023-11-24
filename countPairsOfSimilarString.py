class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if i != j:
                    if sorted(set(words[i])) == sorted(set(words[j])):
                        count = count + 1
        return count
