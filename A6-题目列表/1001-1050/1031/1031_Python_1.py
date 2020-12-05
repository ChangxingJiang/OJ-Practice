from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxSumTwoNoOverlap(A=[0, 6, 5, 2, 2, 5, 1, 9, 4], L=1, M=2))  # 20
    print(Solution().maxSumTwoNoOverlap(A=[3, 8, 1, 3, 2, 1, 8, 9, 0], L=3, M=2))  # 29
    print(Solution().maxSumTwoNoOverlap(A=[2, 1, 5, 6, 0, 9, 5, 0, 3, 8], L=4, M=3))  # 31
