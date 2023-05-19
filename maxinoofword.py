class Solution(object):
    def mostWordsFound(self, sentences):
        arr = []
        for i in range(len(sentences)):
            arr.append(sentences[i].count(" ")+1)
        ans = max(arr)
        return ans
