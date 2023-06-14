class Solution:
    def sortSentence(self, s: str) -> str:
        str_arr = s.split(" ")
        ss = ""
        i = 0
        index = 1
        while index<=len(str_arr):
            for i in range(len(str_arr)):
                if(int(str_arr[i][-1]) == index):
                    ss = ss + str_arr[i][:len(str_arr[i])-1]+" "
                    index = index + 1
        return ss[:len(ss)-1]
            
