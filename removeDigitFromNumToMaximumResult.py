class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        number = list(number)
        if(number.count(digit) == 1):
            number.pop(number.index(digit))
            number = ''.join(number)
            return number
        else:
            indices = [i for i in range(len(number)) if number[i] == digit]
            maxi = 0
            i = 0
            while i< len(indices):
                temp = number[:indices[i]] + number[indices[i]+1:]
                temp = int(''.join(temp))
                maxi = max(temp, maxi)
                i = i + 1
            return str(maxi)


        
