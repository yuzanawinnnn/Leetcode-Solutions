class Solution:
    def countLargestGroup(self, n: int) -> int:
        arr = {}
        count = 0
        for i in range(1,n+1):
            sum_digit = sum(list(map(int,list(str(i)))))
            if sum_digit not in arr:
                arr[sum_digit] = 1
            else:
                arr[sum_digit] = arr[sum_digit] + 1
        for key, value in arr.items():
            if(value == max(arr.values())):
                count = count + 1
        return count



            
