class Solution(object):
    def strStr(self, haystack, needle):
        if(needle not in haystack):
            return -1
        else:
            return haystack.index(needle)
