class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        Heavy = False
        Bulky = False
        if(length >= 10**4 or width>=10**4 or height >=10**4 or length*width*height >= 10**9):
            Bulky = True
        if(mass >=100):
            Heavy = True
        if(Bulky == True and Heavy==True):
            return "Both"
        elif(Bulky == False and Heavy==False):
            return "Neither"
        elif(Bulky == True and Heavy==False):
            return "Bulky"
        elif(Bulky == False and Heavy==True):
            return "Heavy"
