class Solution(object):
    def findTheDifference(self, s, t):
        dicti = list(t)
        text = list(s)
        ans = ""
        empty = False
        for j in range(len(dicti)):
            if(dicti[j] in text):
                text[text.index(dicti[j])] = ""
            else:
                ans = ans + dicti[j]
        return ans
   
 
