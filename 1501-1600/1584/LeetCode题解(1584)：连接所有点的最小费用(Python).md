# LeetCode题解(1584)：连接所有点的最小费用(Python)

题目：[原题链接](https://leetcode-cn.com/problems/min-cost-to-connect-all-points/)（中等）

标签：图、广度优先搜索、堆、并查集

| 解法           | 时间复杂度       | 空间复杂度 | 执行用时        |
| -------------- | ---------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2log(N^2))$ | $O(N^2)$   | 1412ms (56.02%) |
| Ans 2 (Python) |                  |            |                 |
| Ans 3 (Python) |                  |            |                 |

解法一：

```python
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
```

