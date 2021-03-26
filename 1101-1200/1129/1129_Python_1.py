import collections
from typing import List


def build_graph(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_graph = build_graph(red_edges)
        blue_graph = build_graph(blue_edges)

        ans = [-1] * n

        # 先红色边的情况
        visited_red = {0}
        visited_blue = set()
        queue = collections.deque([0])
        step = 0
        while queue:
            for _ in range(len(queue)):
                n1 = queue.popleft()
                if ans[n1] == -1 or ans[n1] > step:
                    ans[n1] = step
                if step % 2 == 0:
                    for n2 in red_graph[n1]:
                        if n2 not in visited_blue:
                            visited_blue.add(n2)
                            queue.append(n2)
                else:
                    for n2 in blue_graph[n1]:
                        if n2 not in visited_red:
                            visited_red.add(n2)
                            queue.append(n2)
            step += 1

        # 先蓝色边的情况
        visited_red = set()
        visited_blue = {0}
        queue = collections.deque([0])
        step = 0
        while queue:
            for _ in range(len(queue)):
                n1 = queue.popleft()
                if ans[n1] == -1 or ans[n1] > step:
                    ans[n1] = step
                if step % 2 == 0:
                    for n2 in blue_graph[n1]:
                        if n2 not in visited_red:
                            visited_red.add(n2)
                            queue.append(n2)
                else:
                    for n2 in red_graph[n1]:
                        if n2 not in visited_blue:
                            visited_blue.add(n2)
                            queue.append(n2)
            step += 1

        return ans


if __name__ == "__main__":
    # [0,1,-1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]))

    # [0,1,-1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[2, 1]]))

    # [0,-1,-1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[1, 0]], blue_edges=[[2, 1]]))

    # [0,1,2]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]]))

    # [0,1,1]
    print(Solution().shortestAlternatingPaths(n=3, red_edges=[[0, 1], [0, 2]], blue_edges=[[1, 0]]))

    # [0,1,2,3,7]
    print(Solution().shortestAlternatingPaths(n=5,
                                              red_edges=[[0, 1], [1, 2], [2, 3], [3, 4]],
                                              blue_edges=[[1, 2], [2, 3], [3, 1]]))

    # [0,2,-1,-1,-1]
    print(Solution().shortestAlternatingPaths(n=5,
                                              red_edges=[[3, 2], [4, 1], [1, 4], [2, 4]],
                                              blue_edges=[[2, 3], [0, 4], [4, 3], [4, 4], [4, 0], [1, 0]]))
