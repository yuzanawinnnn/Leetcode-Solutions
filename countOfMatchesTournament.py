class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n>1:
            if(n%2==0):
                n = int(n/2)
                matches = matches + n
            else:
                n = int((n-1)/2) + 1
                matches = matches + n -1
        return matches
