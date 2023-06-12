class Solution(object):
    def maxScore(self, s):
        string1 = ""
        string2 = ""
        arr = []
        for i in range(len(s)-1):
            string1 = s[:i+1]
            string2 = s[i+1:]
            arr.append(string1.count('0')+string2.count('1'))
        return max(arr)


