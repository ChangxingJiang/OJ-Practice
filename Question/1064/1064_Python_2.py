from typing import List


class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1

        ans = -1
        while l <= r:
            m = (l + r) // 2
            if A[m] < m:
                l = m + 1
            elif A[m] > m:
                r = m - 1
            else:
                ans = m
                r = m - 1

        return ans


if __name__ == "__main__":
    print(Solution().fixedPoint([-10, -5, 0, 3, 7]))  # 3
    print(Solution().fixedPoint([0, 2, 5, 8, 17]))  # 0
    print(Solution().fixedPoint([-10, -5, 3, 4, 7, 9]))  # -1
