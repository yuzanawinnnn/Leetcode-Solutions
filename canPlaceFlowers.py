class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flower = n
        j = 0
        if(len(flowerbed)==1 and flowerbed[0] == 0):
            return True
        elif(len(flowerbed)==1 and n==0):
            return True
        elif(len(flowerbed)>1):
            while j<len(flowerbed) and flower>0:
                if(j==0):
                    if(flowerbed[j+1] ==0 and flowerbed[j]==0):
                        flowerbed[j] = 1
                        flower = flower -1
                elif(j==len(flowerbed)-1):
                    if(flowerbed[j-1]==0 and flowerbed[j]==0):
                        flowerbed[j] = 1
                        flower = flower -1
                else:
                    if(flowerbed[j-1]==0 and flowerbed[j+1] ==0 and flowerbed[j]==0):
                        flowerbed[j] = 1
                        flower = flower -1
                j = j + 1
            if(flower == 0):
                return True
            else:
                return False

