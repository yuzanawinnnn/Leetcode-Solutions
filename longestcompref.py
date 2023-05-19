class Solution(object):
    def longestCommonPrefix(self, strs):
        s = min(strs, key=len)
        ans = ""
        flag = False
        for i in range(len(s)):
            temp = s[:i+1]
            for j in range(len(strs)):
                if(temp != strs[j][:i+1] and flag!= True):
                    flag = True
            if(flag == False):
                ans = temp[:i+1]
        return ans       
