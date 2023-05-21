class Solution(object):
    def uniqueMorseRepresentations(self, words):
        moose = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        arr = set()
        for i in range(len(words)):
            s =""
            for j in range(len(words[i])):
                s = s + moose[ord(words[i][j]) - 97]
            arr.add(s)
        return len(arr)
