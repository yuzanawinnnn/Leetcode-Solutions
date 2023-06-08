class Solution(object):
    def countConsistentStrings(self, allowed, words):
        arr = list(allowed)
        count = 0
        for i in range(len(words)):
            j = 0
            found = False
            while found == False and j<len(words[i]):
                if(words[i][j] not in arr):
                    found = True
                j = j + 1
            if(found == False):
                count = count + 1
        return count
