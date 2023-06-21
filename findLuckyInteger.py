class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = []
        unique_arr = list(set(arr))
        for i in range(len(unique_arr)):
            if(arr.count(unique_arr[i]) == unique_arr[i]):
                lucky.append(unique_arr[i])
        if(len(lucky) == 0):
            return -1
        else:
            return lucky[-1]
