from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], word1="coding",
                                      word2="practice"))  # 3
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], word1="makes",
                                      word2="coding"))  # 1
