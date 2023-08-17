class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = [i for i, x in enumerate(nums) if x == key]
        arr = []
        for j in range(len(nums)):
            found = False
            m = 0
            while found == False and m<len(indices):
                if( abs(j - indices[m]) <= k):
                    found = True
                m = m + 1 
            if(found == True):
                arr.append(j)
        return arr
