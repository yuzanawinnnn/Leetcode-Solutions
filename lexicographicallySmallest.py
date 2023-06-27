class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        rev_str = s[::-1]
        smaller = list(min(rev_str,s))
        bigger = list(max(rev_str,s))
        print(smaller,bigger)
        for i in range(len(s)):
            if(bigger[i] > smaller[i]):
                bigger[i] = smaller[i]
        
        ans = ''.join(bigger)
        return ans
