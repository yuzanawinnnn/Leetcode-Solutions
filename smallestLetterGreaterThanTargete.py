class Solution(object):
    def nextGreatestLetter(self, letters, target):
        alpha = list(map(chr, range(97, 123)))
        found = False
        i = alpha.index(target)+1
        while found !=True and i <len(alpha):
            if(alpha[i] in letters):
                ans = alpha[i]
                found = True
            i = i + 1
        if(found == False):
            return letters[0]
        else:
            return ans
            
