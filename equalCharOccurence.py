class Solution(object):
    def areOccurrencesEqual(self, s):
        a = "".join(set(s))
        count  = set()
        for i in a:
            count.add(s.count(i))
        if(len(count)==1):
            return True
        else:
            return False
