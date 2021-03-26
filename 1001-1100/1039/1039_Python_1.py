import functools
from typing import List


class Solution:
    def minScoreTriangulation(self, array: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i + 1 == j:
                return 0
            res = 10 ** 6 + 1
            for k in range(i + 1, j):
                res = min(res, dp(i, k) + dp(k, j) + array[i] * array[j] * array[k])
            return res

        return dp(0, len(array) - 1)


if __name__ == "__main__":
    print(Solution().minScoreTriangulation([1, 2, 3]))  # 6
    print(Solution().minScoreTriangulation([3, 7, 4, 5]))  # 144
    print(Solution().minScoreTriangulation([1, 3, 1, 4, 1, 5]))  # 13
    print(Solution().minScoreTriangulation([4, 3, 1, 3]))  # 24
