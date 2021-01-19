import functools
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)

        @functools.lru_cache(None)
        def dfs(i1, i2):
            if i1 == n1 or i2 == n2:
                return 0
            if A[i1] == B[i2]:
                return 1 + dfs(i1 + 1, i2 + 1)
            else:
                return max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))

        return dfs(0, 0)


if __name__ == "__main__":
    # 2
    print(Solution().maxUncrossedLines(A=[1, 4, 2],
                                       B=[1, 2, 4]))

    # 3
    print(Solution().maxUncrossedLines(A=[2, 5, 1, 2, 5],
                                       B=[10, 5, 2, 1, 5, 2]))

    # 2
    print(Solution().maxUncrossedLines(A=[1, 3, 7, 1, 7, 5],
                                       B=[1, 9, 2, 5, 1]))
