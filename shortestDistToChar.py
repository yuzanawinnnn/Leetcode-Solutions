class Solution(object):
    def shortestToChar(self, s, c):
        arr = []
        index = []
        for i in range(len(s)):
            if(s[i] == c):
                index.append(i)
        for j in range(len(s)):
            distance = []
            for k in range(len(index)):
                distance.append(abs(j-index[k]))
            arr.append(min(distance))
        return arr
            
