from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)

        window = size - k
        now = sum(cardPoints[:window])

        ans = now
        for i in range(window, size):
            now += cardPoints[i] - cardPoints[i - window]
            ans = min(ans,now)
        return sum(cardPoints) - ans


if __name__ == "__main__":
    print(Solution().maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))  # 12
    print(Solution().maxScore(cardPoints=[2, 2, 2], k=2))  # 4
    print(Solution().maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))  # 55
    print(Solution().maxScore(cardPoints=[1, 1000, 1], k=1))  # 1
    print(Solution().maxScore(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3))  # 202
