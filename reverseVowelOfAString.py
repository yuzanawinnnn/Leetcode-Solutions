class Solution(object):
    def reverseVowels(self, s):
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        arr = []
        s = list(s)
        for i in range(len(s)):
            if(s[i] in vowel):
                arr.append(s[i])
        rev_arr = arr[::-1]
        k = 0
        res = ""
        for j in range(len(s)):
            if s[j] in vowel:
                res = res + rev_arr[k]
                k = k + 1
            else:
                res = res + s[j]
        return res
            
