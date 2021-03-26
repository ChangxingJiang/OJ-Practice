import collections
from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        count = [0] * n  # 记录入度数量
        graph = [[] for _ in range(n)]  # 记录出度的图

        for x, y in richer:
            count[y] += 1
            graph[x].append(y)

        queue = collections.deque()
        for i, v in enumerate(count):
            if v == 0:
                queue.append(i)

        # 拓扑排序状态转移
        dp = [i for i in range(n)]
        while queue:
            i1 = queue.popleft()
            for i2 in graph[i1]:
                if quiet[dp[i1]] < quiet[dp[i2]]:
                    dp[i2] = dp[i1]
                count[i2] -= 1
                if count[i2] == 0:
                    queue.append(i2)

        return dp


if __name__ == "__main__":
    # [5,5,2,5,4,5,6,7]
    print(Solution().loudAndRich(richer=[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                                 quiet=[3, 2, 5, 4, 6, 1, 7, 0]))
