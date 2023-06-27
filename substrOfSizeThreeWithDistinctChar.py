class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        count = 0
        while i<len(s)-2:
            if len(list(set(list(s[i:i+3])))) == 3:
                count = count + 1
            i = i + 1
        return count

