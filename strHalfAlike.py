class Solution(object):
    def halvesAreAlike(self, s):
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        first = s[0:int(len(s)/2)]
        count1 = 0
        count2 = 0
        second = s[int(len(s)/2):len(s)]
        for i in range(int(len(s)/2)):
            if(first[i] in vowel):
                count1 = count1 +1 
            if(second[i] in vowel):
                count2 = count2 +1
        if(count1 == count2):
            return True
        else:
            return False
