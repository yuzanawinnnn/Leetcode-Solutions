class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        i = 0
        while i<len(words):
            if(separator in words[i]):
                arr = words[i].split(separator)
                print(arr)
                while ('' in arr):
                    arr.remove('')
                words = words[:i]+ arr + words[i+1:]
                i = i + len(arr)
            else:
                i = i + 1
        return words
