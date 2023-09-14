class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = list(s)
        start = 0
        i = 0
        index = []
        while i<len(arr):
            if(arr[i]==")"):
                found = False
                k = i - 1
                while found == False:
                    if(k == start):
                        index.append(start)
                        index.append(i)
                        start = i + 1
                        found = True
                    elif(arr[k]=="("):
                        arr[k] = "open"
                        arr[i] = "close"
                        found = True
                    else:
                        k = k - 1
            i = i + 1
        index = index[::-1]
        s = list(s)
        for j in range(len(index)):
            s.pop(index[j])
        s = ''.join(s)
        return s
