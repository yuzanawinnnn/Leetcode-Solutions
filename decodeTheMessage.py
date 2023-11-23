class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = list(map(chr, range(97, 123)))
        arr = []
        answer = ""
        key = key.replace(" ","")
        for j in key:
            if(j not in arr):
                arr.append(j)
        for i in message:
            if(i != " "):
                answer = answer + alpha[arr.index(i)]
            else:
                answer = answer + " "
        return answer

        
        
