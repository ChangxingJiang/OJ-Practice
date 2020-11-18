# LeetCode题解(1559)：二维网格图中探测环(Python)

题目：[原题链接](https://leetcode-cn.com/problems/detect-cycles-in-2d-grid/)（困难）

标签：图、深度优先搜索、广度优先搜索、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 636ms (83%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])

        # 寻找所有需要检查的字符
        visited = collections.defaultdict(set)  # 需要检查的字符
        for i in range(n):
            for j in range(m):
                value = grid[i][j]

                # 判断当前位置是否已被查询过，如果已被查询过则跳过
                if (i, j) in visited[value]:
                    continue

                # 如果没被查询过则检查是否存在环
                new_visited = set()
                positions = collections.deque([(None, (i, j))])

                while positions:
                    from_position, now_position = positions.popleft()

                    if now_position not in new_visited:
                        new_visited.add(now_position)
                    else:
                        # 如果检查出环则直接返回结果
                        return True

                    i, j = now_position
                    if i > 0 and grid[i - 1][j] == value and from_position != (i - 1, j):
                        positions.append(((i, j), (i - 1, j)))
                    if i < n - 1 and grid[i + 1][j] == value and from_position != (i + 1, j):
                        positions.append(((i, j), (i + 1, j)))
                    if j > 0 and grid[i][j - 1] == value and from_position != (i, j - 1):
                        positions.append(((i, j), (i, j - 1)))
                    if j < m - 1 and grid[i][j + 1] == value and from_position != (i, j + 1):
                        positions.append(((i, j), (i, j + 1)))

                # 如果没有检查出环在，则记录检查过的点
                visited[value] |= new_visited

        return False
```