from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().longestOnes(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2))  # 6
    print(Solution().longestOnes(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3))  # 10
