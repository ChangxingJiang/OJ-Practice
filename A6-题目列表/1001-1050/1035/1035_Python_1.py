from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxUncrossedLines(A=[1, 4, 2], B=[1, 2, 4]))  # 2
    print(Solution().maxUncrossedLines(A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]))  # 3
    print(Solution().maxUncrossedLines(A=[1, 3, 7, 1, 7, 5], B=[1, 9, 2, 5, 1]))  # 2
