class Solution(object):
    def divideString(self, s, k, fill):
        arr = []
        start = 0
        end = k
        for i in range(int(len(s)/k)+1):
            if(len(s[start:end])<k and len(s[start:end])!=0):
                sub = k-len(s[start:end])
                temp = s[start:end] + fill * sub
                arr.append(temp)
            elif(len(s[start:end])>=k):
                arr.append(s[start:end])
            start = end 
            end = end + k
     
        return arr
