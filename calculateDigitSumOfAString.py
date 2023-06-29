class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            total = ""
            i = 0
            while i<len(s):
                if(i<len(s)-k+1):
                    total = total + str(sum(list(map(int,list(s[i:i+k])))))
                else:
                    total = total + str(sum(list(map(int,list(s[i:])))))
                i = i + k
            s = total
        return s
