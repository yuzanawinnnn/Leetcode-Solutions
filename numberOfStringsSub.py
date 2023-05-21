class Solution(object):
    def numOfStrings(self, patterns, word):
        count = 0
        for i in range(len(patterns)):
            if(patterns[i] in word):
                count = count +1
        return count
