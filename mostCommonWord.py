class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter
        import re
        banned.append("")
        paragraph = paragraph.lower()
        paragraph = re.sub('[^0-9a-zA-Z\s]+', ' ', paragraph)
        paragraph = paragraph.split(" ")
        count= Counter(paragraph)
        i = 0
        arr = count.most_common()
        while(count.most_common()[i][0] in banned):
            i = i + 1
        return count.most_common()[i][0]
