class Solution:
    def fib(self, n: int) -> int:
        arr = [0,1]
        for i in range(1,n):
            if(i>=len(arr)):
                arr.append(arr[i-1]+arr[i-2])
        if(n==0):
            return 0
        else:
            return arr[-1]+arr[-2]
