class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i = 0
        j = 1
        arr = []
        s = s + " "
        while i<len(s)-1:
            start = i
            end = i
            if(i+j<len(s)-1):
                stop = False
                while(s[i]==s[i+j] and stop == False):
                    end = i+j
                    j = j + 1
                    if(i+j>=len(s)-1):
                        stop = True
                if end-start+1>=3:
                    arr.append([start,end])
            i = end+1
            j = 0
        return arr
