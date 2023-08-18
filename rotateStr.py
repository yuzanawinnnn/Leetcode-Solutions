class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0 
        while i<len(s):
            temp = s[i:] + s[:i]
            if(temp == goal):
                return True
            i = i + 1
        return False

