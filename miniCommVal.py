class Solution(object):
    def getCommon(self, nums1, nums2):
        lst3 = list(set(nums1) & set(nums2))
        if(len(lst3)==0):
            return -1
        else:
            return min(lst3)
