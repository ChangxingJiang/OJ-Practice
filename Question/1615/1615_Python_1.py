import collections
from typing import List


# 生成图中边的集合表示
def build_graph_set(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = build_graph_set(roads)
        for i in range(n):
            for j in range(i + 1, n):
                num = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    num -= 1
                ans = max(ans, num)
        return ans


if __name__ == "__main__":
    print(Solution().maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]))  # 4
    print(Solution().maximalNetworkRank(n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))  # 5
    print(Solution().maximalNetworkRank(n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))  # 5
