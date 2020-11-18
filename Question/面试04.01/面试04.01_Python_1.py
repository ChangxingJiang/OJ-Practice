import collections
from typing import List


# 生成有向图中边的集合表示
def build_graph_set_d(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        graph = build_graph_set_d(graph)

        visited = {start}
        node_list = collections.deque([start])

        while node_list:
            now = node_list.popleft()
            for new in graph[now]:
                if new not in visited:
                    node_list.append(new)
                    visited.add(new)
                    if new == target:
                        return True

        return False


if __name__ == "__main__":
    # True
    print(Solution().findWhetherExistsPath(
        n=3, graph=[[0, 1], [0, 2], [1, 2], [1, 2]],
        start=0, target=2))

    # True
    print(Solution().findWhetherExistsPath(
        n=5,
        graph=[[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]],
        start=0, target=4))

    # False
    print(Solution().findWhetherExistsPath(
        n=12,
        graph=[[0, 1], [1, 2], [1, 3], [1, 10], [1, 11], [1, 4], [2, 4], [2, 6], [2, 9], [2, 10], [2, 4], [2, 5],
               [2, 10], [3, 7], [3, 7], [4, 5], [4, 11], [4, 11], [4, 10], [5, 7], [5, 10], [6, 8], [7, 11], [8, 10]],
        start=2, target=3))
