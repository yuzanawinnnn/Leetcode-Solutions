class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        temp = []
        i = 0
        while i<len(arr):
            found = False
            j = 0
            while found == False and j<len(pieces):
                if(arr[i] == pieces[j][0]):
                    for k in range(len(pieces[j])):
                        temp.append(pieces[j][k])
                    found = True
                    i = i + len(pieces[j]) - 1
                    pieces.pop(j)
                j = j + 1 
            if(found == False):
                return False   
            i = i + 1
        if(temp == arr):
            return True
        else:
            return False
