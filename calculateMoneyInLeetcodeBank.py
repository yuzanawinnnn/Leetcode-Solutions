class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 0
        for i in range(n):
            if(i%7==0):
                amount = monday + 1
                monday = amount
            else:
                amount = amount + 1
            print(amount)
            total = total + amount
        return total
            
