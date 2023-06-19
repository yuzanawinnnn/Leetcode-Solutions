class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arr = []
        nums = nums1 + nums2
        nums.sort()
        used = []
        for i in range(len(nums)):
            found = False
            used_flag = False
            for j in range(len(nums)):
                if(nums[i][0] == nums[j][0] and i!=j and i in used):
                    used_flag = True
                elif(nums[i][0] == nums[j][0] and i!=j and j in used):
                    used_flag = True
                elif(nums[i][0] == nums[j][0] and i!=j and i not in used and j not in used):
                    arr.append([nums[i][0],nums[i][1] + nums[j][1]]) 
                    used.append(j)
                    used.append(i)
                    found = True
            
            if(used_flag == False and found == False):
                arr.append(nums[i])
        return arr
