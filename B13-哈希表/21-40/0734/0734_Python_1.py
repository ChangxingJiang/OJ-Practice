from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().areSentencesSimilar(
        ["great", "acting", "skills"],
        ["fine", "drama", "talent"],
        [["great", "fine"], ["acting", "drama"], ["skills", "talent"]]
    ))
