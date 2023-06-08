class Solution(object):
    def threeConsecutiveOdds(self, arr):
        found = False
        i = 0
        while found == False and i<len(arr)-2:
            if(arr[i]%2 != 0 and arr[i+1]%2!=0 and arr[i+2]%2!=0):
                found = True
            i = i + 1
        if(found == False):
            return False
        else:
            return True           
