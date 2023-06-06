class Solution(object):
    def maxNumberOfBalloons(self, text):
        dicti =['b','a','l','l','o','o','n']
        text = list(text)
        empty = False
        total = 0
        not_found =0
        while empty == False:
            count = 0
            j = 0
            not_found = 0
            for j in range(len(dicti)):
                if(dicti[j] in text):
                    count = count + 1
                    text[text.index(dicti[j])] = ""
                else:
                    not_found = not_found+1
                j = j + 1
            if(count == len(dicti)):
                total = total +1
            if(text.count("") == len(text) or not_found == len(dicti)):
                empty = True

        return total
