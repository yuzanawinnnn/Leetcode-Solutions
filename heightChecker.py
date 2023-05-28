class Solution(object):
    def heightChecker(self, heights):
        count = 0
        arr = sorted(heights)
        for i in range(len(heights)):
            if(arr[i] != heights[i]):
                count = count +1
        return count
