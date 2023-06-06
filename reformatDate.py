class Solution(object):
    def reformatDate(self, date):
        import calendar
        s = date.split(" ")
        month = list(calendar.month_abbr).index(s[1])
        if(month<10):
            month = "0" + str(month)
        day = int(s[0][:-2])
        if(day<10):
            day = "0" + str(day)
        ans = s[2]+"-"+str(month)+"-"+str(day)
        return ans
