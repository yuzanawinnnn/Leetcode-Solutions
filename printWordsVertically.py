class Solution:
    def printVertically(self, s):  
        s = s.split(" ")
        maxi = max([len(x) for x in s])
        result = [""] * maxi
        count = 0
        k = 0
        while count < len(s):
            for i in range(len(s)):
                if(len(s[i])>0):
                    s[i] = list(s[i])
                    result[k] = result[k] + s[i][0]
                    s[i].pop(0)
                    if(len(s[i]) == 0):
                        count = count + 1
                    if(count == len(s)):
                        break
                else:
                    result[k] = result[k] + " "
            result[k] = result[k].rstrip()
            k = k + 1
        return result


