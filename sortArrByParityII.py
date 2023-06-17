class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr = list(map(int, range(0, len(nums))))
        even = 0
        odd = 1
        for i in range(len(nums)):
            if(nums[i]%2==0):
                arr[even] = nums[i]
                even = even + 2
            elif(nums[i]%2!=0):
                arr[odd] = nums[i]
                odd = odd + 2
        return arr
                
            

        return arr
