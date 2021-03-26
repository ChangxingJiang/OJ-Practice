import collections
from typing import List


class WordDistance:

    def __init__(self, words: List[str]):
        self.count = collections.defaultdict(list)
        self.size = len(words)
        for i in range(len(words)):
            self.count[words[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        lst1, lst2 = self.count[word1], self.count[word2]
        ans = self.size
        i1, i2 = 0, 0
        while i1 < len(lst1) and i2 < len(lst2):
            idx1, idx2 = lst1[i1], lst2[i2]
            ans = min(ans, abs(idx1 - idx2))
            if idx1 < idx2:
                i1 += 1
            else:
                i2 += 1
        return ans


if __name__ == "__main__":
    obj = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(obj.shortest("coding", "practice"))  # 3
    print(obj.shortest("makes", "coding"))  # 1
