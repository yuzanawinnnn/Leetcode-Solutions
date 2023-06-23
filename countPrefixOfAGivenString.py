class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in range(len(words)):
            if(words[i] == s[:len(words[i])]):
                count = count + 1
        return count
