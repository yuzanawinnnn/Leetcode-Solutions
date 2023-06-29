class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = {}
        for i in range(lowLimit,highLimit+1):
            if sum(list(map(int,list(str(i))))) not in box:
                box[sum(list(map(int,list(str(i)))))] = 1
            else:
                box[sum(list(map(int,list(str(i)))))] = box[sum(list(map(int,list(str(i)))))] + 1
        return max(box.values())
