class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        if(len(grid[0])==1):
            return grid[0][0]
        length = len(grid[0])
        end = False
        j = 0
        while j<length:
            temp = 0
            for i in range(len(grid)):
                grid[i].sort()
                if(temp < grid[i][-1]):
                    temp = grid[i][-1]
                grid[i] = grid[i][:len(grid[i])-1]
            total = total + temp
            j = j + 1
        return total
            
