class Solution(object):
    def sortPeople(self, names, heights):
        arr = []
        i = 0
        while i<len(heights):
            tallest = max(heights)
            person  = names[heights.index(tallest)]
            arr.append(person)
            heights[heights.index(tallest)] = 0
            i = i +1
            
        return arr




        
