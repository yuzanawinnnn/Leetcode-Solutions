class Solution(object):
    def greatestLetter(self, s):
        ans = ""
        arr = []
        for i in s:
            ss = s.lower()
            if(ss.count(i) > 1):
                lower = i.lower()
                upper = i.upper()
                if(lower in s and upper in s):
                    arr.append(i.upper())
            if(len(arr)>0):
                ans = max(arr)
        
        return ans
                                   
