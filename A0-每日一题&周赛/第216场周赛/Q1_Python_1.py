from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


if __name__ == "__main__":
    print(Solution().arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))
