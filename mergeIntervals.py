class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        end = False
        while end == False:
            i = 0
            count = 0
            while i<len(intervals)-1:
                if(intervals[i][1] >= intervals[i+1][0]):
                    intervals[i] = intervals[i] + intervals[i+1]
                    intervals[i].sort()
                    intervals[i] = [intervals[i][0],intervals[i][-1]]
                    intervals.pop(i+1)
                else:
                    count = count + 1
                i = i +1
            if(count==len(intervals)-1):
                end = True
        return intervals
