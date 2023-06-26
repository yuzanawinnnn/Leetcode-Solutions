class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        arr = []
        mini_index = len(list1)+ len(list2)
        for i in range(len(list1)):
            if(list1[i] in list2):
                if(list2.index(list1[i]) + i < mini_index):
                    mini_index = list2.index(list1[i]) + i 
                    arr = []
                    arr.append(list1[i])
                elif(list2.index(list1[i]) + i == mini_index):
                    arr.append(list1[i])
        return arr
