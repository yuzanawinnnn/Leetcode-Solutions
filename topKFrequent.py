class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        arr =[]
        count= Counter(nums)
        for letter, count in count.most_common(k):
            arr.append(letter)
        return arr
