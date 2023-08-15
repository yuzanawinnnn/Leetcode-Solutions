class Solution:
    def countAsterisks(self, s: str) -> int:
        start = None
        count = 0
        for i in range(len(s)):
            if(s[i] == "*"):
                if(start == None):
                    count = count + 1
            elif(s[i] == "|"):
                if(start == None):
                    start = i
                else:
                    start = None
        return count
