class Solution(object):
    def digitCount(self, num):
        found = False
        for i in range(len(num)):
            digit = str(i)
            if(num.count(digit) != int(num[i])):
                found = True
        if(found == True):
            return False
        else:
            return True
