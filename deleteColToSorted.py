class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for j in range(len(strs[0])):
            temp = []
            for i in range(len(strs)):
                temp.append(strs[i][j])
            sorted_arr = sorted(temp)
            if(temp != sorted_arr):
                count = count + 1
        return count
                
            
