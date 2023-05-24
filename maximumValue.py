class Solution(object):
    def maximumValue(self, strs):
        arr =[]
        for i in range(len(strs)):
            if(strs[i].isdigit() == True):
                arr.append(int(strs[i]))
            else:
                arr.append(len(strs[i]))
        return max(arr)
