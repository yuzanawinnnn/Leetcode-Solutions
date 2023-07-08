class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2,num+1):
            sum_digit = sum(list(map(int,list(str(i)))))
            if(sum_digit%2==0):
                count = count + 1
        return count
