from functools import lru_cache
from math import inf
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        s1, s2 = len(cost), len(cost[0])

        # O(M×N)
        min_val = [min(cost[i][j] for i in range(s1)) for j in range(s2)]

        @lru_cache(None)
        def dfs(idx, used):
            # 当第一组已经全部连接完成的情况
            if idx == s1:
                ans = 0
                for j in range(s2):
                    if not used & (1 << j):  # 如果第二组还有尚未连接的点，则用最小成本连接它
                        ans += min_val[j]
                return ans

            # 当第一组还没完全连接完成的情况
            res = inf
            for j in range(s2):
                # 状态转移方程：在每次新增一个第一组的链接时，只考虑增加一个第二组，不考虑第一组同时与多个第二组链接
                res = min(res, cost[idx][j] + dfs(idx + 1, used | (1 << j)))
            return res

        return dfs(0, 0)


if __name__ == "__main__":
    print(Solution().connectTwoGroups(cost=[[15, 96], [36, 2]]))  # 17
    print(Solution().connectTwoGroups(cost=[[1, 3, 5], [4, 1, 1], [1, 5, 3]]))  # 4
    print(Solution().connectTwoGroups(cost=[[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))  # 10
    print(Solution().connectTwoGroups(cost=[[93, 56, 92], [53, 44, 18], [86, 44, 69], [54, 60, 30]]))  # 172
    print(Solution().connectTwoGroups(cost=[
        [42, 79, 85, 15, 74, 100],
        [93, 26, 16, 31, 8, 54],
        [52, 28, 7, 3, 99, 75],
        [5, 26, 73, 23, 84, 82],
        [32, 100, 93, 88, 63, 61],
        [19, 33, 82, 45, 15, 45]
    ]))  # 129
