class Solution(object):
    def vowelStrings(self, words, left, right):
        count = 0
        vowel =['a','e','i','o','u']
        for i in range(left,right+1):
            if(words[i][0] in vowel and words[i][-1] in vowel):
                count = count +1
        return count
