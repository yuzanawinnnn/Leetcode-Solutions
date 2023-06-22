class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        found = False
        i = 0
        ans = ""
        while found == False and i<len(words):
            if(words[i] == words[i][::-1]):
                ans = words[i]
                found = True
            i = i + 1
        return ans
