class Solution(object):
    def secondHighest(self, s):
        arr = []
        for i in range(len(s)):
            if(s[i].isdigit() == True and int(s[i]) not in arr):
                arr.append(int(s[i]))
        if(len(arr)<2):
            return -1
        else:
            arr.sort()
            return arr[len(arr)-2]

