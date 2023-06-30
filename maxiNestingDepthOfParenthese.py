class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        brackets = []
        for i in range(len(s)):
            if(s[i] =="("):
                brackets.append("(")
            elif(s[i] ==")"):
                depth = max(depth,len(brackets))
                brackets.pop(-1)
        return depth
                
