class Solution(object):
    def makeFancyString(self, s):
        ss = list(s)
        string = ""
        for i in range(len(ss)-2):
            if(ss[i] == ss[i+1] and ss[i+1] == ss[i+2]):
                continue
            else:
                string = string + ss[i]
        if(len(s)>2):
            string = string + ss[len(ss)-2] + ss[len(ss)-1]
        elif(len(s)==2):
            string = ss[0] + ss[1]
        else:
            string = ss[0]
        return string
        
