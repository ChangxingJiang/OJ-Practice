from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().bagOfTokensScore(tokens=[100], P=50))  # 0
    print(Solution().bagOfTokensScore(tokens=[100, 200], P=150))  # 1
    print(Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], P=200))  # 2
