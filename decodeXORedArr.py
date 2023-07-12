class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr=[first]
        for i in range(len(encoded)):
            arr.append(encoded[i]^arr[i])
        return arr
