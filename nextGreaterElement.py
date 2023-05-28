class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        arr = []
        for i in range(len(nums1)):
            if(nums2.index(nums1[i]) == len(nums2)-1):
                arr.append(-1)
            elif(nums2.index(nums1[i]) != len(nums2)-1):
                j = nums2.index(nums1[i])
                found = False
                while found == False and j<len(nums2):
                    if(nums2[j]>nums1[i]):
                        arr.append(nums2[j])
                        found = True
                    j = j + 1
                if(found == False):
                    arr.append(-1)
        return arr

