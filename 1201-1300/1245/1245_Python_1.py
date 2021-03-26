import collections
import heapq
from typing import List


# 生成无向图中边的集合表示
def build_graph_set(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:
    def __init__(self):
        self.ans = 0
        self.graph = collections.defaultdict(set)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        self.graph = build_graph_set(edges)
        self.dfs(0, -1)
        return self.ans

    def dfs(self, node, parent):
        lengths = [self.dfs(child, node) for child in self.graph[node] if child != parent]
        if len(lengths) == 0:
            return 0
        elif len(lengths) == 1:
            self.ans = max(self.ans, lengths[0] + 1)
            return lengths[0] + 1
        else:
            n1, n2 = heapq.nlargest(2, lengths)
            self.ans = max(self.ans, n1 + n2 + 2)
            return max(n1, n2) + 1


if __name__ == "__main__":
    # 2
    print(Solution().treeDiameter([[0, 1], [0, 2]]))

    # 4
    print(Solution().treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
