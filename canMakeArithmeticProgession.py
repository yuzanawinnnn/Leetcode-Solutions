class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        i = 1
        diff = sorted_arr[1]-sorted_arr[0]
        found = False
        while found == False and i<len(sorted_arr):
            if(sorted_arr[i]-sorted_arr[i-1] != diff):
                found = True
            i = i + 1
        if(found == True):
            return False
        else:
            return True
