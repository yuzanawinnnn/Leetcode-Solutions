class Solution(object):
    def flipAndInvertImage(self, image):
        arr = []
        for i in range(len(image)):
            reverse = image[i][::-1]    
            for j in range(len(reverse)):
                if(reverse[j]==1):
                    reverse[j]=0
                else:
                    reverse[j]=1
            arr.append(reverse)
        return arr
