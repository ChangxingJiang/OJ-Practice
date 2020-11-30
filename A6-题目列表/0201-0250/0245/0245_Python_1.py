from typing import List


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    # 1
    print(Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],
                                          word1="makes", word2="coding"))

    # 3
    print(Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],
                                          word1="makes", word2="makes"))
