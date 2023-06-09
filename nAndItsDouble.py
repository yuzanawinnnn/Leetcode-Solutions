class Solution(object):
    def checkIfExist(self, arr):
        found = False
        i = 0
        while found == False and i <len(arr):
            j = 0
            while found == False and j<len(arr):
                if(i!=j and arr[i] == arr[j]*2):
                    found = True
                j = j + 1
            i = i + 1
        if(found == False):
            return False
        else:
            return True
