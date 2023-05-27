class Solution(object):
    def largestGoodInteger(self, num):
        arr = [""]
        for i in range(len(num)):
            temp = num[i:i+3]
            if(len(temp) == 3):
                if(temp[0]==temp[1] and temp[1]==temp[2]):
                    arr.append(temp)

        return max(arr)
