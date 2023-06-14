class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(len(a)<len(b)):
            a = "0"*(len(b)-len(a)) + a
        elif(len(a)>len(b)):
            b = "0"*(len(a)-len(b)) + b
        s = ""
        temp = "0"
        for i in range(len(a)-1,-1,-1):
            arr = [a[i],b[i],temp]
            if(arr.count("0") == 3):
                s = s + "0"
                temp = "0"
            elif(arr.count("1")==3):
                s = s + "1"
                temp = "1"
            elif(arr.count("1")==2):
                s = s + "0"
                temp = "1"
            elif(arr.count("1")==1):
                s = s + "1"
                temp = "0"
        if(temp =="1"):
            s = s + "1"

        return s[::-1]
            
            
