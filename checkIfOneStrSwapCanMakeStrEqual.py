class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if(s1 == s2):
            return True
        s1 = list(s1)
        s2 = list(s2)
        i = 0
        end = False
        arr = []
        while end == False and i<len(s1):
            if(s1[i] != s2[i] and len(arr) == 0):
                arr.append(i)
            elif(s1[i] != s2[i] and len(arr) == 1):
                temp = s1[arr[0]]
                s1[arr[0]] = s1[i]
                s1[i] = temp
                end = True
            i = i + 1
        if(s1 == s2):
            return True
        elif(end == False):
            return False
        else:
            return False

                    
