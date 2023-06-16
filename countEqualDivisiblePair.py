class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        from itertools import combinations
        number = list(map(int, range(0, len(nums))))
        arr = list(combinations(number,2))
        count = 0
        used = []
        for i in range(len(arr)):
            if(nums[arr[i][0]]==nums[arr[i][1]] and (arr[i][0]*arr[i][1])%k == 0 and used.append(arr[i][0]) not in used and used.append(arr[i][1]) not in used):
                count = count + 1
                used.append(arr[i][0])
                used.append(arr[i][1])
        return count


