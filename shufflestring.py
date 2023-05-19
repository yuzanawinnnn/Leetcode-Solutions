class Solution(object):
    def restoreString(self, s, indices):
        ans = ""
        for i in range(len(indices)):
            temp = min(indices)
            ans = ans + s[indices.index(temp)]
            indices[indices.index(temp)] = len(indices)+1
        return ans
