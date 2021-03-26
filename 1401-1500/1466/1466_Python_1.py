from typing import List


def build_graph_set(edges):
    import collections
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add((edge[1], 1))
        graph[edge[1]].add((edge[0], 0))
    return graph


class Solution:
    def __init__(self):
        self.ans = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = build_graph_set(connections)

        def dfs(node1, father=None):
            for node2, point in graph[node1]:
                if node2 != father:
                    self.ans += point
                    dfs(node2, node1)

        dfs(0)

        return self.ans


if __name__ == "__main__":
    # 3
    print(Solution().minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))

    # 2
    print(Solution().minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))

    # 0
    print(Solution().minReorder(n=3, connections=[[1, 0], [2, 0]]))
