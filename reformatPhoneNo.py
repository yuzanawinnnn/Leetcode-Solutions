class Solution:
    def reformatNumber(self, number: str) -> str:
        import re
        number = re.sub(r'[^0-9]', '', number)
        phoneNo = ""
        i = 0
        while i<len(number):
            if(i<len(number)-4):
                phoneNo = phoneNo + number[i:i+3] + "-"
                i = i + 3
            elif(i==len(number)-4):
                phoneNo = phoneNo + number[i:i+2] + "-" + number[i+2:]
                i = len(number)
            else:
                phoneNo = phoneNo + number[i:] 
                i = len(number)
        return phoneNo
