class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        i = 0
        count = 0
        while len(num_str) - i >= k:
            if(int(num_str[i:i+k]) != 0):
                if(num % int(num_str[i:i+k]) == 0):
                    count = count + 1
            i = i + 1
        return count

