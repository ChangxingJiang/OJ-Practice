from functools import lru_cache
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dfs(left: int, right: int) -> int:
            if left == right:
                return 0

            total = sum(stoneValue[left:right + 1])
            sum1 = ans = 0
            for i in range(left, right):
                sum1 += stoneValue[i]
                sum2 = total - sum1
                if sum1 < sum2:
                    ans = max(ans, dfs(left, i) + sum1)
                elif sum1 > sum2:
                    ans = max(ans, dfs(i + 1, right) + sum2)
                else:
                    ans = max(ans, max(dfs(left, i), dfs(i + 1, right)) + sum1)
            return ans

        n = len(stoneValue)
        return dfs(0, n - 1)


if __name__ == "__main__":
    # 18
    print(Solution().stoneGameV(stoneValue=[6, 2, 3, 4, 5, 5]))

    # 28
    print(Solution().stoneGameV(stoneValue=[7, 7, 7, 7, 7, 7, 7]))

    # 0
    print(Solution().stoneGameV(stoneValue=[4]))

    print(Solution().stoneGameV(
        stoneValue=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100, 100, 100, 100, 100,
                    100, 100, 100, 100, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 10000, 10000, 10000,
                    10000, 10000, 10000, 10000, 10000, 10000, 10000, 100000, 100000, 100000, 100000, 100000, 100000,
                    100000, 100000, 100000, 100000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000,
                    1000000, 1000000, 1000000]))

    # 330
    print(Solution().stoneGameV(stoneValue=[98, 77, 24, 49, 6, 12, 2, 44, 51, 96]))
