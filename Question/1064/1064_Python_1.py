from typing import List


class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i, n in enumerate(A):
            if i == n:
                return i
        return -1


if __name__ == "__main__":
    print(Solution().fixedPoint([-10, -5, 0, 3, 7]))  # 3
    print(Solution().fixedPoint([0, 2, 5, 8, 17]))  # 0
    print(Solution().fixedPoint([-10, -5, 3, 4, 7, 9]))  # -1
