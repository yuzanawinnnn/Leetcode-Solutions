class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dicti = {}
        arr = []
        ret = []
        for i in range(len(items1)):
            dicti[items1[i][0]] = items1[i][1]
            arr.append(items1[i][0])
        for j in range(len(items2)):
            if(items2[j][0] not in dicti.keys()):
                dicti[items2[j][0]] = items2[j][1]
                arr.append(items2[j][0])
            else:
                dicti[items2[j][0]] = dicti[items2[j][0]] + items2[j][1]
        arr.sort()
        for k in range(len(arr)):
            ret.append([arr[k],dicti[arr[k]]])
        return ret



