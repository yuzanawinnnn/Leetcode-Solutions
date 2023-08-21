class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        matrix = []
        for i in range(len(score)):
            arr.append(score[i][k])
        arr = sorted(list(set(arr)))
        arr = arr[::-1]
        for j in range(len(arr)):
            for l in range(len(score)):
                if(score[l][k] == arr[j]):
                    matrix.append(score[l])
        return matrix
