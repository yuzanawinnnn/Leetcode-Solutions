class Solution(object):
    def findRelativeRanks(self, score):
        s = sorted(score)
        s = s[::-1]
        for i in range(len(s)):
            if(i == 0):
                score[score.index(s[i])] = "Gold Medal"
            elif(i==1):
                score[score.index(s[i])] = "Silver Medal"
            elif(i==2):
                score[score.index(s[i])] = "Bronze Medal"
            else:
                score[score.index(s[i])] = str(i+1)
        return score
