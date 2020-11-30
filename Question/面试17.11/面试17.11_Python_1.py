from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        i1, i2 = -ans, -ans
        for i, word in enumerate(words):
            if word == word1:
                i1 = i
                ans = min(ans, i1 - i2)
            elif word == word2:
                i2 = i
                ans = min(ans, i2 - i1)
        return ans


if __name__ == "__main__":
    # 1
    print(Solution().findClosest(words=["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"],
                                 word1="a", word2="student"))
