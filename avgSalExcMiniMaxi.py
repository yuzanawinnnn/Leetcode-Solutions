class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        ans = sum(salary[1:len(salary)-1])/(len(salary)-2)
        return ans
