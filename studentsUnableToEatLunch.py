class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while len(sandwiches)>0 and sandwiches[0] in students:
            if(students[0] != sandwiches[0]):
                students.append(students[0])
                students.pop(0)
            elif(students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
        count = len(sandwiches)
        return count
