class Solution(object):
    def oddString(self, words):
        alpha = list(map(chr, range(97, 123)))
        arr = []
        arr_set = set()
        temp = 0
        for i in range(len(words)):
            int_arr = []
            for j in range(len(words[i])-1,0,-1):
                int_arr.append(alpha.index(words[i][j])- alpha.index(words[i][j-1]))
            arr.append(int_arr)
        found = False
        k =0
        while found == False:
            if(arr.count(arr[k]) == 1):
                ans = words[k]
                found = True
            k = k +1
        return ans
