class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]
        start = 0
        end = 1
        while end<len(n):
            if((end+1-start)%3==0 and end+1 != len(n)):
                n = n[:end+1]+"."+n[end+1:]
                start = end + 2
                end = end + 2
            else:
                end = end + 1
        return n[::-1]
