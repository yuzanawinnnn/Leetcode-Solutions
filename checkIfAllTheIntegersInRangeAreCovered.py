class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        i = 0
        j = left
        not_cover = False
        while not_cover == False and j<=right:
            if(j>=ranges[i][0] and j<=ranges[i][1]):
                    j = j + 1
                    i = 0
            else:
                i = i + 1
                if(i==len(ranges)):
                    not_cover = True
                    return False
        if not_cover == False:
            return True
