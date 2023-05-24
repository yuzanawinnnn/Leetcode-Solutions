class Solution(object):
    def numUniqueEmails(self, emails):
        arr = set()
        for i in range(len(emails)):
            s = ""
            skip = False
            index = emails[i].index("@")
            for j in range(len(emails[i])):
                if(skip == True and emails[i][j]=="@"):
                    s = s[0:s.index("+")] + "@"
                elif(j > index):
                    s = s + emails[i][j]
                elif(emails[i][j]!='.' and emails[i][j]!='+'):
                    s = s + emails[i][j]
                elif(emails[i][j]=='.'):
                    s = s
                elif(emails[i][j]=='+'):
                    skip = True
                    s = s + "+"
            
            arr.add(s)
        return(len(arr))
