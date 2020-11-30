# LeetCode题解(0694)：不同岛屿的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-distinct-islands/)（中等）

标签：哈希表、图、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 236ms (75.76%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        islands = set()

        size1, size2 = len(grid), len(grid[0])
        for i1 in range(size1):
            for i2 in range(size2):
                if grid[i1][i2] == 0 or (i1, i2) in visited:
                    continue

                land, min1, min2, max1, max2 = {(i1, i2)}, i1, i2, i1, i2
                pos_list = collections.deque([(i1, i2)])
                while pos_list:
                    i3, i4 = pos_list.popleft()
                    if i3 + 1 < size1 and grid[i3 + 1][i4] == 1 and (i3 + 1, i4) not in land:
                        land.add((i3 + 1, i4))
                        pos_list.append((i3 + 1, i4))
                        max1 = max(max1, i3 + 1)
                    if i4 + 1 < size2 and grid[i3][i4 + 1] == 1 and (i3, i4 + 1) not in land:
                        land.add((i3, i4 + 1))
                        pos_list.append((i3, i4 + 1))
                        max2 = max(max2, i4 + 1)
                    if i3 - 1 >= 0 and grid[i3 - 1][i4] == 1 and (i3 - 1, i4) not in land:
                        land.add((i3 - 1, i4))
                        pos_list.append((i3 - 1, i4))
                        min1 = min(min1, i3 - 1)
                    if i4 - 1 >= 0 and grid[i3][i4 - 1] == 1 and (i3, i4 - 1) not in land:
                        land.add((i3, i4 - 1))
                        pos_list.append((i3, i4 - 1))
                        min2 = min(min2, i4 - 1)

                island = []
                for i3 in range(min1, max1 + 1):
                    row = []
                    for i4 in range(min2, max2 + 1):
                        if (i3, i4) in land:
                            row.append("1")
                        else:
                            row.append("0")
                    island.append("".join(row))
                island = " ".join(island)

                visited |= land
                islands.add(island)

        return len(islands)

```