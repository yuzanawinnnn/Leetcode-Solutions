class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        second = 0
        while tickets[k] != 0:
            i = 0
            while tickets[k] !=0 and i<(len(tickets)):
                if(tickets[i] > 0):
                    tickets[i] = tickets[i] - 1
                    second = second + 1
                i = i + 1
                
        return second
