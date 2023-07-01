class Solution:
    def dayOfYear(self, date: str) -> int:
        day = [31,28,31,30,31,30,31,31,30,31,30,31]
        date = date.split("-")
        month = int(date[1])
        total = int(date[2])
        for i in range(month-1):
            total = total + day[i]
            if(i==1 and int(date[0])%4==0 and int(date[0])!=1900):
                total = total + 1
        return total
        
            

