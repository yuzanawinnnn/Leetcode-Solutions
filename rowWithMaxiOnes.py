class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        arr = []
        for i in range(len(mat)):
            arr.append(mat[i].count(1))
        return [arr.index(max(arr)),max(arr)]
