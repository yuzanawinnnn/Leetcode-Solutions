class Solution(object):
    def prefixCount(self, words, pref):
        count = 0
        for i in range(len(words)):
            if( pref == words[i][:len(pref)]):
                count = count +1
        return count
