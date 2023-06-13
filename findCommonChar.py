class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = []
        for i in range(len(words[0])):
            found = False
            j = 0
            while found == False and j<len(words):
                if(j!=0 and words[0][i] in words[j]):
                    index = words[j].index(words[0][i])
                    words[j]= words[j][:index]+words[j][index+1:]
                elif(j!=0 and words[0][i] not in words[j]):
                    found = True
                j = j + 1
            if found == False:
                arr.append(words[0][i])
        return arr
