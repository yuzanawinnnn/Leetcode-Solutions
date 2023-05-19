class Solution(object):
    def interpret(self, command):
        s = ''
        for i in range(len(command)):
            if(command[i]=="(" and command[i+1]==")"):
                s = s+ "o"
            elif(command[i]=="(" and command[i+1]!=")"):
                s = s 
            elif(command[i]==")"):
                s = s
            else: 
                s = s + command[i]
        return s
