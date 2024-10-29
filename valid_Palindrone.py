class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ''.join(ch for ch in s if ch.isalnum())
        if(s1 == s1[::-1]):
            return True
        else:
            return False
