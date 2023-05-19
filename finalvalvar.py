class Solution(object):
    def finalValueAfterOperations(self, operations):
        initial = 0
        for i in range(len(operations)):
            if(operations[i] == "X++" or operations[i] == "++X"):
                initial = initial +1
            elif(operations[i] == "X--" or operations[i] =="--X"):
                initial = initial - 1

        return initial 
