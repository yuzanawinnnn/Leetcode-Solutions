class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left,right+1):
            s = str(i)
            j = 0
            found = False
            while j<len(s) and found == False:
                if(s[j] != '0'):
                    if(i%int(s[j]) != 0):
                        found = True
                else:
                    found = True
                j = j + 1
            if(found == False):
                arr.append(i)
        return arr
