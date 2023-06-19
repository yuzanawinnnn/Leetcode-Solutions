class Solution:
    def kWeakestRows(self, mat, k):
        arr = set()
        dicti = {}
        ans = []
        for i in range(len(mat)):
            arr.add(sum(mat[i]))
            dicti[i] = sum(mat[i])
        arr = list(arr)
        arr.sort()
        for j in range(len(arr)):
            for key,val in dicti.items():
                if(val == arr[j]):
                    ans.append(key)
        return ans[:k]
