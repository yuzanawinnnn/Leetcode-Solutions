class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        for i in range(k):
            gifts[gifts.index(max(gifts))] = int(math.sqrt(max(gifts)))
        return sum(gifts)
