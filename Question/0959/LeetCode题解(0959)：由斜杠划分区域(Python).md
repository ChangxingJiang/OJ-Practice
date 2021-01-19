# LeetCode题解(0959)：由斜杠划分区域(Python)

题目：[原题链接](https://leetcode-cn.com/problems/regions-cut-by-slashes/)（中等）

标签：并查集、图、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 216ms (55.79%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class DSU1:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n

    def find(self, i: int):
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int):
        i, j = self.find(i), self.find(j)
        if self._size[i] >= self._size[j]:
            self._array[j] = i
            self._size[i] += self._size[j]
        else:
            self._array[i] = j
            self._size[j] += self._size[i]

    def group_num(self):
        groups = set()
        for i in range(len(self._array)):
            if self._array[i] not in groups:
                j = self.find(i)
                if j not in groups:
                    groups.add(self.find(i))
        return len(groups)


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        size = len(grid)
        dsu = DSU1(size * size * 4)  # 将每个点视作4个点：上=0,左=1,下=2,右=3

        # 链接所有边缘位置：左右、上下
        for i in range(size):
            for j in range(size):
                # 连接边缘位置
                if i > 0:
                    dsu.union((i * size + j) * 4, ((i - 1) * size + j) * 4 + 2)
                if j > 0:
                    dsu.union((i * size + j) * 4 + 1, (i * size + (j - 1)) * 4 + 3)

                if grid[i][j] == " ":
                    dsu.union((i * size + j) * 4, (i * size + j) * 4 + 1)
                    dsu.union((i * size + j) * 4 + 1, (i * size + j) * 4 + 2)
                    dsu.union((i * size + j) * 4 + 2, (i * size + j) * 4 + 3)
                elif grid[i][j] == "\\":
                    dsu.union((i * size + j) * 4 + 1, (i * size + j) * 4 + 2)
                    dsu.union((i * size + j) * 4, (i * size + j) * 4 + 3)
                else:  # grid[i][j] == "/"
                    dsu.union((i * size + j) * 4, (i * size + j) * 4 + 1)
                    dsu.union((i * size + j) * 4 + 2, (i * size + j) * 4 + 3)

        return dsu.group_num()
```

