class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        j = startIndex
        k = startIndex
        count = 0
        found = False
        for i in range(len(words)):
            if words[j] == target or words[k] == target :
                found = True
                break
            j = j + 1
            k = k - 1

            if(j==len(words)):
                j = 0
            if(k==-1):
                k = len(words)-1
            count = count + 1
        if(found == True):
            return count
        else:
            return -1

