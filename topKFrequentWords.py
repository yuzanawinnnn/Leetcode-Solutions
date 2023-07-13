class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        arr = []
        words.sort()
        count= Counter(words)
        for letter, count in count.most_common(k):
            arr.append(letter)
        return arr
