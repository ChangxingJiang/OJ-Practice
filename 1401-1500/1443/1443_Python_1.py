from typing import List


def build_graph_set(edges):
    import collections
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = build_graph_set(edges)

        def dfs(node1, father=-1):
            val = 0
            for node2 in graph[node1]:
                if node2 != father:
                    val += dfs(node2, node1)

            if val or hasApple[node1]:
                return val + 2
            else:
                return 0

        return dfs(0) - 2 if dfs(0) else 0


if __name__ == "__main__":
    # 8
    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, True, False, True, True, False]))

    # 6
    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, True, False, False, True, False]))

    # 0
    print(Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], hasApple=[False, False, False, False, False, False, False]))
