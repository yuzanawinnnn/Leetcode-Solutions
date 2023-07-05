class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        found = False
        i = 2
        while found == False:
            if(i%2==0 and i%n==0):
                return i
            else:
                i = i + 1
