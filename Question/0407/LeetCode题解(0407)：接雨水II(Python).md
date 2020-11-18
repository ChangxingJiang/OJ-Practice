# LeetCode题解(0407)：接雨水II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/trapping-rain-water-ii/)（困难）

标签：堆、广度优先搜索

| 解法           | 时间复杂度      | 空间复杂度 | 执行用时       |
| -------------- | --------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NMlog(N+M))$ | $O(N+M)$   | 144ms (80.58%) |
| Ans 2 (Python) |                 |            |                |
| Ans 3 (Python) |                 |            |                |

解法一（海平面上升思路）：

```python
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 判断位置是否有效
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        # 海平面不断升高淹没盆地思路
        s1, s2 = len(heightMap), len(heightMap[0])
        s = s1 * s2

        # 处理池子过小的情况
        # O(1)
        if s1 <= 2 or s2 <= 2:
            return 0

        # 计算最外层堤坝位置
        # O(M+N)
        wall_list = []
        for i1 in range(0, s1):
            wall_list.append((i1, 0))
            wall_list.append((i1, s2 - 1))
        for i2 in range(0, s2):
            wall_list.append((0, i2))
            wall_list.append((s1 - 1, i2))

        # 处理最外层堤坝高度
        visited = set()
        heap = []
        for i1, i2 in wall_list:
            heap.append((heightMap[i1][i2], i1, i2))
            visited.add((i1, i2))

        # 使最外层堤坝高度具有堆的特征
        heapq.heapify(heap)

        # 初始化海平面高度
        now_height = 0

        # 开始提升海平面高度直至只剩下狭长（中间不包括被堤坝包围的陆地）岛屿
        ans = 0
        while len(visited) < s:
            # 从堤坝高度堆中取出最低的堤坝
            height, i1, i2 = heapq.heappop(heap)

            # 升高（或不用升高）海平面至可以淹没堤坝的高度
            now_height = max(now_height, height)

            # 计算堤坝周围的坐标位置
            neighbours = [(i1 + 1, i2), (i1 - 1, i2), (i1, i2 + 1), (i1, i2 - 1)]

            # 计算堤坝周围的非堤坝或海洋位置（腹地位置）
            inners = [neighbour for neighbour in neighbours if
                      (is_valid(neighbour[0], neighbour[1]) and neighbour not in visited)]

            # 检查腹地位置的淹没情况
            for ii1, ii2 in inners:
                # 如果腹地位置比当前海平面低，则可以增加积水量
                if heightMap[ii1][ii2] < now_height:
                    ans += now_height - heightMap[ii1][ii2]

                # 将当前腹地位置作为新的堤坝
                heapq.heappush(heap, (heightMap[ii1][ii2], ii1, ii2))
                visited.add((ii1, ii2))

        return ans
```