class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums1)):
            if(nums1[i] == 0 and len(nums2)>0):
                nums1[i] = nums2[0]
                nums2.pop(0)
        nums1.sort()
