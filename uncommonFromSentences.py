class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        arr = set()
        i = 0
        j = 0
        flag = False
        while flag == False:
            if(i<len(s1)):
                if(s1[i] not in s2 and s1.count(s1[i]) == 1):
                    arr.add(s1[i])
            if(i<len(s2)):
                if(s2[i] not in s1 and s2.count(s2[i]) == 1):
                    arr.add(s2[i])
            if(i>= len(s1) and i>=len(s2)):
                flag = True
            i = i +1
        return list(arr)
            
                
                
        
