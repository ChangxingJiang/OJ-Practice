from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pass


if __name__ == "__main__":
    # True
    print(Solution().isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))

    # False
    print(Solution().isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))

    # False
    print(Solution().isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
