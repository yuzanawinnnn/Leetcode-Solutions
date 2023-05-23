class Solution(object):
    def squareIsWhite(self, coordinates):
        alpha = ['a','b','c','d','e','f','g','h']
        index = alpha.index(coordinates[0]) + 1 
        if(int(coordinates[1])%2 != 0 and index%2 !=0):
            return False
        elif(int(coordinates[1])%2 != 0 and index%2 ==0):
            return True
        elif(int(coordinates[1])%2 == 0 and index%2 ==0):
            return False
        elif(int(coordinates[1])%2 == 0 and index%2 !=0):
            return True
        
