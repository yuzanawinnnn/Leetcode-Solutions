class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num>0:
            if(num%2==0):
                num = int(num/2)
            else:
                num = num - 1
            count = count + 1
        return count
