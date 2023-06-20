class Solution:
    def checkDistances(self, s, distance):
        alpha = list(map(chr,range(97,123)))
        i = 0
        count = 0
        err = False
        used = []
        while count<int(len(s)/2) and err == False:
            if(s[i] not in used):
                if(abs(s[i+1:].index(s[i])) == distance[alpha.index(s[i])]):
                    count = count + 1
                    used.append(s[i])
                else:
                    err = True
            i = i + 1
        if(err == True):
            return False
        else:
            return True
