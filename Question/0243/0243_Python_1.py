from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1

        ans = len(words)

        for i, word in enumerate(words):
            if word == word1:
                i1 = i
                if i2 != -1:
                    ans = min(ans, i1 - i2)
            elif word == word2:
                i2 = i
                if i1 != -1:
                    ans = min(ans, i2 - i1)

        return ans


if __name__ == "__main__":
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], word1="coding",
                                      word2="practice"))  # 3
    print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], word1="makes",
                                      word2="coding"))  # 1
