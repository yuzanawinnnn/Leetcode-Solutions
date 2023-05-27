class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        s = sentence.split(" ")
        found = False
        i = 0
        index = -1
        while found == False and i<len(s):
            if(searchWord == s[i][:len(searchWord)]):
                found = True
                index = i+1
            i = i + 1
        return index
            
