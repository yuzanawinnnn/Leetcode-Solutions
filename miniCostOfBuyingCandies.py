class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost = cost[::-1]
        total = 0

        while len(cost)>1:
            total = total + cost[0]+cost[1]
            if(len(cost)>2):
                if(cost[2]<=cost[1]):
                    cost.pop(2)
                    cost.pop(1)
                    cost.pop(0)
                else:
                    cost.pop(1)
                    cost.pop(0)
            else:
                cost.pop(1)
                cost.pop(0)
        if(len(cost)==1):
            total = total + cost[0]
        return total
