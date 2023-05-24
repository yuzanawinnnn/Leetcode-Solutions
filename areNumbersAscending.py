class Solution(object):
    def areNumbersAscending(self, s):
        ss = s.split(" ")
        arr = []
        flag = False
        for i in range(len(ss)):
            if(ss[i].isdigit() == True):
                if(int(ss[i]) in arr):
                    flag = True
                        
                arr.append(int(ss[i]))
        
        print(arr)
        sort = sorted(arr)
        if(flag == True):
            return False
        elif(arr == sort):
            return True
        else:
            return False
