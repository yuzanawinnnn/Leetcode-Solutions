class Solution(object):
    def countWords(self, words1, words2):
        arr = []
        count = 0
        for i in range(len(words1)):
            if(words1.count(words1[i]) == 1):
                arr.append(words1[i])
        for j in range(len(words2)):
            if(words2.count(words2[j]) ==1 and words2[j] in arr):
                count = count +1
        return count
