class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        first = str(int(s[::-1]))
        second = int(first[::-1])
        if second == num:
            return True
        else:
            return False
