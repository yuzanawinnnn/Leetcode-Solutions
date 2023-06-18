class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            sorted_arr = sorted(stones)
            if(sorted_arr[-1]==sorted_arr[-2]):
                stones.pop(stones.index(sorted_arr[-1]))
                sorted_arr.pop(-1)
                stones.pop(stones.index(sorted_arr[-1]))
                sorted_arr.pop(-1)
            elif(sorted_arr[-1]!=sorted_arr[-2]):
                stones[stones.index(sorted_arr[-1])] = sorted_arr[-1] - sorted_arr[-2]
                stones.pop(stones.index(sorted_arr[-2]))
                sorted_arr.pop(-2)
        if(len(stones)<1):
            return 0
        else:
            return stones[-1]
                
