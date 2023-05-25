class Solution(object):
    def createTargetArray(self, nums, index):
        target = []
        for j in range(len(nums)):
            target.append("")        
        for i in range(len(nums)):
            if(target[index[i]] == ""):
                target[index[i]] = nums[i]
            else:
                temp = target[0:index[i]]
                temp.append(nums[i])
                target = temp + target[index[i]:]
        return target[0:len(nums)]
