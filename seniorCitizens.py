class Solution(object):
    def countSeniors(self, details):
        count = 0
        for i in range(len(details)):
            age = int(details[i][11]+details[i][12])
            if(age>60):
                count = count +1
        return count
