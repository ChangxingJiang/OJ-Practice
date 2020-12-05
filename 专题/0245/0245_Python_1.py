from typing import List


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        # 处理不同单词的情况
        if word1 != word2:
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

        # 处理相同单词的情况
        else:
            i1 = -1
            ans = len(words)

            for i, word in enumerate(words):
                if word == word1:
                    if i1 != -1:
                        ans = min(ans, i - i1)
                    i1 = i

            return ans


if __name__ == "__main__":
    # 1
    print(Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],
                                          word1="makes", word2="coding"))

    # 3
    print(Solution().shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"],
                                          word1="makes", word2="makes"))
