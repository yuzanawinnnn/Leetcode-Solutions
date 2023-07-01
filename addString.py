class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num1 = num1[::-1]
        num2 = list(num2)
        num2 = num2[::-1]
        s = ""
        temp = 0
        
        i = 0
        end = False
        while end == False:
            if(i<len(num1) and i<len(num2)):
                s = s + str((int(num1[i])+int(num2[i])+temp)%10)
                temp = (int(num1[i])+int(num2[i])+temp)//10
            elif(i<len(num1)):
                s = s + str((int(num1[i])+temp)%10)
                temp = (int(num1[i])+temp)//10
            elif(i<len(num2)):
                s = s + str((int(num2[i])+temp)%10)
                temp = (int(num2[i])+temp)//10
            elif(temp!=0):
                s = s + str(temp)
                temp = 0
            else:
                end = True
            i = i + 1
        return s[::-1]
        


                
