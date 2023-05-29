class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr = []
        left = []
        index =[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr.append(arr1[j])
                if arr1[j] not in arr2 and j not in index:
                    left.append(arr1[j])
                    index.append(j)
        left.sort()
        ans = arr + left
        return ans
