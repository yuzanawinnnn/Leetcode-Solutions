class Solution(object):
    def stringMatching(self, words):
        arr = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if(words[i] in words[j] and i != j):
                    arr.add(words[i])
        return list(arr)
