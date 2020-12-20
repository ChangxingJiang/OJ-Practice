from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        pass


if __name__ == "__main__":
    # 23
    print(Solution().maxScoreWords(words=["dog", "cat", "dad", "good"],
                                   letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                                   score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                          0]))

    # 27
    print(Solution().maxScoreWords(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"],
                                   score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0,
                                          10]))

    # 0
    print(Solution().maxScoreWords(words=["leetcode"], letters=["l", "e", "t", "c", "o", "d"],
                                   score=[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                                          0]))
