class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        alpha = list(map(chr, range(97, 123)))
        first = ""
        second = ""
        target = ""
        for i in range(len(firstWord)):
            first = first + str(alpha.index(firstWord[i]))
        for j in range(len(secondWord)):
            second = second + str(alpha.index(secondWord[j]))
        for k in range(len(targetWord)):
            target = target + str(alpha.index(targetWord[k]))  
        if(int(target) == int(first) + int(second)):
            return True
        else:
            return False
