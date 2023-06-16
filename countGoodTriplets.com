class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        from itertools import combinations
        result_arr = []
 
        aa = list(combinations(arr, 3))
        for i in range(len(aa)):
            if(abs(aa[i][0]-aa[i][1])<=a and abs(aa[i][1]-aa[i][2])<=b and abs(aa[i][2]-aa[i][0])<=c):
                result_arr.append(aa[i])
        return len(result_arr)
