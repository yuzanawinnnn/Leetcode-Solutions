class Solution(object):
    def removeTrailingZeros(self, num):
        count = 0
        i = len(num)-1
        end = False
        while end == False and i>=0:
            if(num[i] != '0'):
                end = True
            else:
                count = count + 1
            i = i - 1
        if(end == False):
            return num
        else:
            num = num [:len(num)-count]
            return num
