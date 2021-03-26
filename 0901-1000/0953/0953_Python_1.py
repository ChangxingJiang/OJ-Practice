from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for (c1, c2) in zip(word1, word2):
                if order.index(c1) < order.index(c2):
                    break
                elif order.index(c1) > order.index(c2):
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        return True


if __name__ == "__main__":
    # True
    print(Solution().isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz"))

    # False
    print(Solution().isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz"))

    # False
    print(Solution().isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz"))
