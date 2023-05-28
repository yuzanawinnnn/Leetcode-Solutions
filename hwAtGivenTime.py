class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            if(endTime[i]>=queryTime and startTime[i]<=queryTime):
                count = count +1
        return count
        
