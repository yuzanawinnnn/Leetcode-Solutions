class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        arr = []
        result = []
        dicti = {}
        for i in range(len(s)):
            if(s[i] not in dicti.keys()):
                dicti[s[i]] = s.count(s[i])
                arr.append(s.count(s[i]))
        arr.sort()
        arr = arr[::-1]
        for j in range(len(arr)):
            for key, value in dicti.items():
                if value == arr[j]:
                    result.append(key*value)
                    dicti[key] = 0    
        result = ''.join(result)    
        return result
