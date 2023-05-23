class Solution(object):
    def reversePrefix(self, word, ch):
        if ch in word:
            index = word.index(ch)
            s = word[:index+1]
            s = s[::-1] + word[index+1:]
        else:
            s = word
        return s
