class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s = list(set(list(s)))
        s = ''.join(s)
        return len(s)
