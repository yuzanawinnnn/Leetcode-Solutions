class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        not_found = False
        magazine = list(magazine)
        i = 0
        while not_found == False and i<len(ransomNote):
            if(ransomNote[i] not in magazine):
                not_found = True
            else:
                magazine.pop(magazine.index(ransomNote[i]))
            i = i + 1
        if(not_found == False):
            return True
        else:
            return False
