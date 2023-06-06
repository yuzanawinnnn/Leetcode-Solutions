class Solution(object):
    def firstUniqChar(self, s):
        found = False
        i = 0
        while found == False and i<len(s):
            if(s.count(s[i]) ==1):
                ans = i
                found = True
            i = i + 1
        if(found == False):
            ans = -1
        return ans
