class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):

        arr = set()
        for i in range(len(nums1)):
            if(nums1[i] in nums2 or nums1[i] in nums3):
                arr.add(nums1[i])
        for i in range(len(nums2)):
            if(nums2[i] in nums1 or nums2[i] in nums3):
                arr.add(nums2[i])
        for i in range(len(nums3)):
            if(nums3[i] in nums2 or nums3[i] in nums1):
                arr.add(nums3[i])
        return list(arr)
