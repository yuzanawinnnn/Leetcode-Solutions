class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        n = str(n)
        while n!="1":
            total = 0
            for i in range(len(n)):
                total = total + int(n[i])**2
            n = str(total)
            if n not in arr:
                arr.append(n)
            else:
                return False
        return True

            
