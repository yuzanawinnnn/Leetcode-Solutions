class Solution(object):
    def toGoatLatin(self, sentence):
        s = sentence.split(" ")
        ans = ""
        vowel= ['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(s)):
            if(s[i][0] in vowel):
                s[i] = s[i] + "ma" + "a"*(i+1)
            if(s[i][0] not in vowel):
                s[i] = s[i][1:] + s[i][0] + "ma" + "a"*(i+1)
        for j in range(len(s)):
            ans = ans + s[j] + " "
        return ans[:len(ans)-1]

            
