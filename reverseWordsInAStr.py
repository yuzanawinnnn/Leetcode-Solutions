class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(' ')
        reverse = ss[::-1]
        string = ""
        for i in range(len(reverse)):
            if(reverse[i]!=''):
                string = string + reverse[i] + " "
        return string[:len(string)-1]
        
            
