class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagrams = []
        i = 0
        while i<len(strs):
            temp = []
            if(strs[i] != "!"):
                temp = [strs[i]]
                for j in range(len(strs)):
                    if len(strs[i]) == len(strs[j]) and i != j and strs[j]!= "!":
                        if sorted(strs[i]) == sorted(strs[j]):
                            temp.append(strs[j])
                            strs[j] = "!"
            strs[i] = "!"
            if(temp != []):
                Anagrams.append(temp)
            i = i + 1
        return Anagrams
