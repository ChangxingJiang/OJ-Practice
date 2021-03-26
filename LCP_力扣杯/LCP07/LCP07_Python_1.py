import collections
from typing import List


def build_graph(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        graph = build_graph(relation)
        aim = n - 1

        def dfs(now, kk):
            if kk == 0:
                return 1 if now == aim else 0
            else:
                res = 0
                for child in graph[now]:
                    res += dfs(child, kk - 1)
                return res

        return dfs(0, k)


if __name__ == "__main__":
    print(Solution().numWays(n=5, relation=[[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], k=3))  # 3
    print(Solution().numWays(n=3, relation=[[0, 2], [2, 1]], k=2))  # 0
