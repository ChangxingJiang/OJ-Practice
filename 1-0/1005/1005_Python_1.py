from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().largestSumAfterKNegations(A=[4, 2, 3], K=1))  # 5
    print(Solution().largestSumAfterKNegations(A=[3, -1, 0, 2], K=3))  # 6
    print(Solution().largestSumAfterKNegations(A=[2, -3, -1, 5, -4], K=2))  # 13
