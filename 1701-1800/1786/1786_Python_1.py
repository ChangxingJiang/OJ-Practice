import collections
import functools
import heapq
from typing import List


# 生成无向图加权中边的邻接列表结构
def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    return graph


class Solution:
    _MOD = 10**9+7
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # 将边存储到字典结构中
        graph = build_graph(edges)

        # 计算所有点距离结点n的距离
        distances = {}
        cloud = [[0, n]]
        while cloud:
            while cloud and cloud[0][1] in distances:
                heapq.heappop(cloud)
            if not cloud:
                break
            d, i = heapq.heappop(cloud)
            distances[i] = d
            for j in graph[i]:
                if j not in distances:
                    heapq.heappush(cloud, [d + graph[i][j], j])

        # 记忆化递归计算受限路径数量
        @functools.lru_cache(None)
        def dfs(n1):
            if n1 == 1:
                return 1
            res = sum(dfs(n2) for n2 in graph[n1] if distances[n2] > distances[n1])
            return res

        return dfs(n) % self._MOD


if __name__ == "__main__":
    # 3
    print(Solution().countRestrictedPaths(n=5, edges=[[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1],
                                                      [5, 4, 10]]))

    # 1
    print(Solution().countRestrictedPaths(n=7, edges=[[1, 3, 1], [4, 1, 2], [7, 3, 4], [2, 5, 3], [5, 6, 1], [6, 7, 2],
                                                      [7, 5, 3], [2, 6, 4]]))
