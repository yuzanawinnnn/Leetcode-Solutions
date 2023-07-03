class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ss = ""
        s = list(s)
        for i in range(len(order)):
            while order[i] in s:
                ss = ss + order[i]
                s.pop(s.index(order[i]))
        s = ''.join(s)
        return ss+s
