class Solution:
    def hardestWorker(self, n, logs):
        arr = []
        maxi = 0
        for i in range(len(logs)):
            if(i == 0):
                prev = 0
            else:
                prev = logs[i-1][1]
            duration = logs[i][1] - prev
            if(maxi < duration):
                arr = []
                arr.append(logs[i][0])
                maxi = duration
            elif(maxi == duration):
                arr.append(logs[i][0])
        arr.sort()
        return arr[0]
