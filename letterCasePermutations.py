class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        import re
        from itertools import combinations
        result = []
        count = len(re.findall('[a-zA-Z]', s))
        arr = ['U','L']*count
        cases = list(set(combinations(arr,count)))
        for i in range(len(cases)):
            temp = list(cases[i])
            ss = ""
            k = 0
            for j in range(len(s)):
                if(s[j].isalpha()==True):
                    if(temp[k]=='U'):
                        ss = ss + s[j].upper()
                        k = k + 1
                    else:
                        ss = ss + s[j].lower()
                        k = k + 1
                else:
                    ss = ss + s[j]
            result.append(ss)
        return result

