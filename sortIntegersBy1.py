class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        count = set()
        pair = []
        ans = []
        arr.sort()
        for i in range(len(arr)):
            binary = str(bin(arr[i]))
            pair.append([binary.count("1"),arr[i]])
            count.add(binary.count("1"))
        count = list(count)
        count.sort()
        for j in range(len(count)):
            for k in range(len(pair)):
                if(count[j] == pair[k][0]):
                    ans.append(pair[k][1])
        return ans


            
