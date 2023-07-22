class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = list(map(int,nums))
        n.sort()
        n = n[::-1]
        return str(n[k-1])
