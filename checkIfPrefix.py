class Solution(object):
    def isPrefixString(self, s, words):
        full = False
        ss = ""
        i = 0
        while full == False and i <len(words):
            ss = ss + words[i]
            if(ss == s):
                full = True
            i = i + 1
        if(ss == s):
            return True
        else:
            return False
