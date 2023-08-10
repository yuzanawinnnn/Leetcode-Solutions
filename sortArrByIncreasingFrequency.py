class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        a = []
        array = []
        nums.sort()
        nums = nums[::-1]
        for i in range(len(nums)):
            if(nums[i] not in counter.keys()):
                counter[nums[i]] = nums.count(nums[i])
                a.append(nums.count(nums[i]))
        a.sort()
        j = 0
        for j in range(len(a)):
            for keys, values in counter.items():
                if(values == a[j]):
                    for m in range(values):
                        array.append(keys)
                    counter[keys] = 0
        nums = array
        return nums
