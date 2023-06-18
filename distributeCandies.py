class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        type = list(set(candyType))
        can_eat = int(len(candyType)/2)
        return min(len(type),can_eat)
