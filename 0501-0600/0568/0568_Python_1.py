import collections
from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n, k = len(flights), len(days[0])

        # 构造邻接列表格式的图
        # 有向图（不一定是对称的）
        graph = collections.defaultdict(set)
        for city1 in range(n):
            for city2 in range(n):
                if flights[city1][city2]:
                    graph[city2].add(city1)  # 城市j可以由i到达

        # 按周和城市动态规划
        dp = [float("-inf")] * n
        dp[0] = 0
        for week in range(k):
            new = [float("-inf")] * n
            for city2 in range(n):
                new[city2] = dp[city2] + days[city2][week]
                for city1 in graph[city2]:
                    new[city2] = max(new[city2], dp[city1] + days[city2][week])
            dp = new

        return int(max(dp))


if __name__ == "__main__":
    print(Solution().maxVacationDays(flights=[[0, 1, 1],
                                              [1, 0, 1],
                                              [1, 1, 0]],
                                     days=[[1, 3, 1],
                                           [6, 0, 3],
                                           [3, 3, 3]]))  # 12
    print(Solution().maxVacationDays(flights=[[0, 0, 0],
                                              [0, 0, 0],
                                              [0, 0, 0]],
                                     days=[[1, 1, 1],
                                           [7, 7, 7],
                                           [7, 7, 7]]))  # 3
    print(Solution().maxVacationDays(flights=[[0, 1, 1],
                                              [1, 0, 1],
                                              [1, 1, 0]],
                                     days=[[7, 0, 0],
                                           [0, 7, 0],
                                           [0, 0, 7]]))  # 21
