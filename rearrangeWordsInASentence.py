class Solution:
    def arrangeWords(self, text: str) -> str:
        t = text.lower()
        t = t.split(" ")
        length = []
        word = []
        for i in range(len(t)):
            l = len(t[i])
            if(l in length):
                j = len(length) - 1
                while(l != length[j]):
                    j = j - 1
                word = word[:j+1]+[t[i]]+word[j+1:]
                length = length[:j+1]+[l]+length[j+1:]
            elif(len(length) > 0 and l < length[-1]):
                j = len(length) - 1
                while(l<length[j] and j>=0):
                    j = j - 1
                if(j<0):
                    word = [t[i]]+word
                    length = [l]+length
                else:
                    word = word[:j+1]+[t[i]]+word[j+1:]
                    length = length[:j+1]+[l]+length[j+1:]

            else:
                word.append(t[i])
                length.append(len(t[i]))
        word[0] = ''.join(list(list(word[0])[0].upper()) + list(word[0])[1:])
        word = ' '.join(word)
        return word
                
