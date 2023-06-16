class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr = []
        arr1 = []
        arr2 = []
        i = 0
        j = 0
        while i <len(nums1):
            if(nums1[i] not in nums2 and nums1[i] not in arr1):
                arr1.append(nums1[i])
            i = i + 1
        arr.append(arr1)
        while j <len(nums2):
            if(nums2[j] not in nums1 and nums2[j] not in arr2):
                arr2.append(nums2[j])
            j = j + 1
        arr.append(arr2)
        return arr
            
