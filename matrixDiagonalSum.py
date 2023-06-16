class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(i == j or j==len(mat[i])-i-1):
                    total = total + mat[i][j]
        return total
