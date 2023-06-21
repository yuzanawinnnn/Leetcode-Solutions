class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        arr = []
        for i in range(len(nums)):
            if(i%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort()
        odd = odd[::-1]
        k = 0
        l = 0
        for j in range(len(nums)):
            if(j%2==0):
                arr.append(even[k])
                k = k + 1
            else:
                arr.append(odd[l])
                l = l + 1
        return arr

