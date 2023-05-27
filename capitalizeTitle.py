class Solution(object):
    def capitalizeTitle(self, title):
        s = ""
        title = title.split(" ")
        for i in range(len(title)):
            if(len(title[i])>=3):
                title[i] = title[i].lower()
                title[i] = title[i][0].upper()+title[i][1:]
                s = s + title[i]+" "
            else:
                title[i] = title[i].lower()
                s = s + title[i]+" "
        return s[:len(s)-1]
