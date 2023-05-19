class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        dicti = {"type":0,"color":1,"name":2}
        count = 0
        for i in range(len(items)):
            temp = dicti[ruleKey]
            if(items[i][temp] == ruleValue ):
                count = count + 1
        return count
                
