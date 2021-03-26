import collections
from typing import List


class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m and (x, y) not in broken

        def get_near(x, y):
            return [(x1, y1) for (x1, y1) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if is_valid(x1, y1)]

        visited = [[False] * m for _ in range(n)]
        broken = set((i, j) for (i, j) in broken)

        ans = 0

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and (i, j) not in broken:
                    # 广度优先搜索遍历当前区域
                    visited[i][j] = True
                    queue = collections.deque([(i, j)])
                    points = [(i, j)]
                    while queue:
                        i1, j1 = queue.popleft()
                        for i2, j2 in get_near(i1, j1):
                            if not visited[i2][j2]:
                                visited[i2][j2] = True
                                queue.append((i2, j2))
                                points.append((i2, j2))

                    # 思路：二分图中黑点和白点 + 贪心算法，从只有一个选择的点开始选择

                    # 构造图
                    graph = {point: set() for point in points}
                    for (i1, j1) in graph:
                        for i2, j2 in get_near(i1, j1):
                            graph[(i1, j1)].add((i2, j2))

                    # 贪心选择
                    while len(graph) >= 2:
                        for (i1, j1) in list(graph.keys()):
                            for i2, j2 in list(graph[(i1, j1)]):
                                if (i2, j2) not in graph:
                                    graph[(i1, j1)].remove((i2, j2))
                            if len(graph[(i1, j1)]) == 0:
                                del graph[(i1, j1)]

                        min_idx, min_val = (-1, -1), 5
                        for (i1, j1) in list(graph.keys()):
                            if len(graph[(i1, j1)]) < min_val:
                                min_idx, min_val = (i1, j1), len(graph[i1, j1])
                                if min_val == 1:
                                    break

                        if min_val < 5:
                            i1, j1 = min_idx
                            i2, j2 = graph[min_idx].pop()

                            del graph[(i1, j1)]
                            del graph[(i2, j2)]
                            ans += 1

        return ans


if __name__ == "__main__":
    # 2
    print(Solution().domino(n=2, m=3, broken=[[1, 0], [1, 1]]))

    # 4
    print(Solution().domino(n=3, m=3, broken=[]))

    # 6
    print(Solution().domino(n=4, m=4, broken=[[1, 1], [2, 2]]))

    # 14
    #   0 1 2 3 4 5 6 7
    # 0 O X O O X X O O
    # 1 X O O O X O O X
    # 2 O X O X O O X O
    # 3 X X O O O O O O
    # 4 X X X X X O X O
    # 5 X X O O O X X X
    # 6 O O O O X O X X
    # 7 O O X O X X O X
    print(Solution().domino(n=8, m=8,
                            broken=[[0, 1], [0, 4], [0, 5], [1, 0], [1, 4], [1, 7], [2, 1], [2, 3], [2, 6], [3, 0],
                                    [3, 1], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 6], [5, 0], [5, 1], [5, 5],
                                    [5, 6], [5, 7], [6, 4], [6, 6], [6, 7], [7, 2], [7, 4], [7, 5], [7, 7]]))

    # 28
    print(Solution().domino(n=8, m=8, broken=[[0, 1], [2, 0], [4, 3], [4, 7], [5, 4]]))
