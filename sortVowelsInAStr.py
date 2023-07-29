class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowel = ['a','e','i','o','u']
        arr = []
        index = []
        for i in range(len(s)):
            if(s[i].lower() in vowel):
                arr.append(s[i])
                index.append(i)
        arr.sort()
        for j in range(len(index)):
            s[index[j]] = arr[j]
        s = ''.join(s)
        return s

