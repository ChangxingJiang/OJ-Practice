import heapq
from math import inf
from typing import List


class Solution:
    # Dijkstra算法

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0

        size = len(points)

        # 计算各个点之间距离的邻接矩阵
        # O(N^2)
        min_idx, min_val = (-1, -1), inf  # 最小距离的两个点和最小距离
        distance = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(i + 1, size):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                distance[i][j] = distance[j][i] = d
                if d < min_val:
                    min_idx, min_val = (i, j), d

        # for row in distance:
        #     print(row)

        # ----------Dijkstra算法----------
        ans = min_val  # 使用路径总和

        # 当前云中已经包含的点
        visited = {min_idx[0], min_idx[1]}

        # 当前云连接向外连接的路径长度和目标点
        heap = [(min(distance[i][min_idx[0]], distance[i][min_idx[1]]), i) for i in range(size) if i not in visited]
        heapq.heapify(heap)

        while len(visited) < size:
            # print(ans, visited, heap)

            # 如果云向外链接的目标点已在云内，则放弃它
            while heap[0][1] in visited:
                heapq.heappop(heap)

            d, i = heapq.heappop(heap)
            ans += d
            visited.add(i)

            for j in range(size):
                if j not in visited:
                    heapq.heappush(heap, (distance[i][j], j))

        return ans


if __name__ == "__main__":
    print(Solution().minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # 20
    print(Solution().minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))  # 18
    print(Solution().minCostConnectPoints(points=[[0, 0], [1, 1], [1, 0], [-1, 1]]))  # 4
    print(Solution().minCostConnectPoints(points=[[-1000000, -1000000], [1000000, 1000000]]))  # 4000000
    print(Solution().minCostConnectPoints(points=[[0, 0]]))  # 0
