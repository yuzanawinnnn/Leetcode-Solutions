class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        while "#" in s or "#" in t:
            if("#" in s and s.index("#")!=0):
                index = s.index("#")
                s.pop(index-1)
                s.pop(index-1)
            elif("#" in s and s.index("#")==0):
                index = s.index("#")
                s.pop(index)
            if("#" in t and t.index("#")!=0):
                index = t.index("#")
                t.pop(index-1)
                t.pop(index-1)
            elif("#" in t and t.index("#")==0):
                index = t.index("#")
                t.pop(index)
        if(s == t):
            return True
        else:
            return False




