class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0,10:0,20:0}
        i = 0
        no_change = False
        while no_change == False and i<len(bills):
            if(bills[i] == 5):
                change[5] = change[5] + 1
            elif(bills[i]==10 and change[5] >= 1):
                change[5] = change[5] -1
                change[10] = change [10] + 1
            elif(bills[i]==20 and change[10]>=1 and change[5]>=1):
                change[5] = change[5] - 1
                change[10] = change[10] -1
                change[20] = change [20] + 1
            elif(bills[i]==20 and change[5]>=3):
                change[5] = change[5] - 3
                change[20] = change [20] + 1
            else:
                no_change = True
            i = i + 1
        if(no_change == True):
            return False
        else:
            return True
        

            
