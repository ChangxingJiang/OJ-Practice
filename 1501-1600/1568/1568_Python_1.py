import collections
from typing import List


# 图
# 所有点均在环上 = 2
# 有的点不在环上 = 1
# 直接分隔 = 0
# O(4×N^2)


class Vertex:
    def __init__(self):
        self.near = set()


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # 生成图的顶点
        G = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    G[(i, j)] = Vertex()

        # 生成图的边
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i > 0 and grid[i - 1][j] == 1:
                        G[(i, j)].near.add(G[(i - 1, j)])
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        G[(i, j)].near.add(G[(i + 1, j)])
                    if j > 0 and grid[i][j - 1] == 1:
                        G[(i, j)].near.add(G[(i, j - 1)])
                    if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                        G[(i, j)].near.add(G[(i, j + 1)])

        # 计算顶点数量
        vertex_count = len(G)

        # 判断图是否为连通图
        start_vertex = list(G.values())[0]
        visited = {start_vertex}
        now_vertex_list = collections.deque([start_vertex])
        while now_vertex_list:
            now_vertex = now_vertex_list.popleft()
            for near_vertex in now_vertex.near:
                if near_vertex not in visited:
                    visited.add(near_vertex)
                    now_vertex_list.append(near_vertex)

        # 如果不是连通图，则不用修改
        if len(visited) != vertex_count:
            return 0

        # 处理连通图且点极少的特殊情况
        if vertex_count == 0:
            return 0
        if vertex_count == 1:
            return 1
        if vertex_count == 2:
            return 2

        # 不在环上的点有两种可能：一种为唯一连接两块大陆，一种是自身是一个半岛
        # 我们将左右各是一块大陆顶点称为陆桥，陆桥的特征：每个邻点直接互不相连
        # 半岛的特征：只有一个邻点

        # 遍历所有的点，判断它们是否为半岛或陆桥
        # 如果包含半岛或陆桥，直接返回1
        for key, now_vertex in G.items():
            # 判断是否为半岛
            if len(now_vertex.near) == 1:
                return 1

            # 判断是否为陆桥
            visited_list = [set() for _ in range(len(now_vertex.near))]

            # 计算各个方向的起点
            start_vertex_list = list(now_vertex.near)

            # 遍历各个方向
            for i in range(len(start_vertex_list)):
                start_vertex = start_vertex_list[i]
                visited_list[i].add(start_vertex)
                now_vertex_list = collections.deque([start_vertex])
                while now_vertex_list:
                    now2_vertex = now_vertex_list.popleft()
                    for near_vertex in now2_vertex.near:
                        if near_vertex not in visited_list[i] and near_vertex != now_vertex:
                            visited_list[i].add(near_vertex)
                            now_vertex_list.append(near_vertex)

            # print(key, now_vertex, len(visited_list), [len(visited) for visited in visited_list])

            if len(visited_list) == 2 and not visited_list[0] & visited_list[1]:
                return 1
            if len(visited_list) == 3 and not visited_list[0] & visited_list[1] & visited_list[2]:
                return 1
            if len(visited_list) == 4 and not visited_list[0] & visited_list[1] & visited_list[2] & visited_list[3]:
                return 1

        return 2


if __name__ == "__main__":
    # 2
    print(Solution().minDays(grid=[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))

    # 2
    print(Solution().minDays(grid=[[1, 1]]))

    # 0
    print(Solution().minDays(grid=[[1, 0, 1, 0]]))

    # 1
    print(Solution().minDays(grid=[[1, 1, 0, 1, 1],
                                   [1, 1, 1, 1, 1],
                                   [1, 1, 0, 1, 1],
                                   [1, 1, 0, 1, 1]]))

    # 2
    print(Solution().minDays(grid=[[1, 1, 0, 1, 1],
                                   [1, 1, 1, 1, 1],
                                   [1, 1, 0, 1, 1],
                                   [1, 1, 1, 1, 1]]))
