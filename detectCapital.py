class Solution(object):
    def detectCapitalUse(self, word):
        if(word.islower()==True):
            return True
        elif(word.isupper()==True):
            return True
        elif(word[0].isupper()== True and word[1:].islower()== True):
            return True
        else:
            return False
