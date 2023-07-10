class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        i = 0
        changed = False
        while changed == False and i<len(num):
            if(num[i]=="6"):
                num[i]="9"
                changed = True
            i = i + 1
        num = int(''.join(num))
        return num
