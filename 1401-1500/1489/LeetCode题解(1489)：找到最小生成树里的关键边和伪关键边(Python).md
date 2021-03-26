# LeetCode题解(1489)：找到最小生成树里的关键边和伪关键边(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)（困难）

标签：并查集、深度优先搜索、图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(E^2)$   | $O(N+E)$   | 1984ms (25.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class DSU1:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n

        self.group_num = n  # 连通分支数量

    def find(self, i: int) -> int:
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int) -> bool:
        i, j = self.find(i), self.find(j)
        if i != j:
            if self._size[i] >= self._size[j]:
                self._array[j] = i
                self._size[i] += self._size[j]
            else:
                self._array[i] = j
                self._size[j] += self._size[i]
            self.group_num -= 1
            return True
        else:
            return False

    def is_connected(self, i: int, j: int) -> bool:
        return self.find(i) == self.find(j)

    def __repr__(self):
        return str(len(self._array)) + ":" + str(self._array)


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        size = len(edges)

        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        # 计算当前情况下的最小生成树的权值最小和
        # O(E)
        dsu = DSU1(n)
        min_power = 0
        for i in range(size):
            if dsu.union(edges[i][0], edges[i][1]):
                min_power += edges[i][2]

        ans = [[], []]
        # 遍历每条边检查是否为关键边或伪关键边
        for i in range(size):
            # 判断是否是关键边
            dsu = DSU1(n)
            power = 0
            for j in range(size):
                if i != j and dsu.union(edges[j][0], edges[j][1]):
                    power += edges[j][2]
            if dsu.group_num != 1 or (dsu.group_num == 1 and power > min_power):
                ans[0].append(edges[i][3])
                continue

            # 判断是否是伪关键边
            dsu = DSU1(n)
            dsu.union(edges[i][0], edges[i][1])
            power = edges[i][2]
            for j in range(size):
                if i != j and dsu.union(edges[j][0], edges[j][1]):
                    power += edges[j][2]
            if power == min_power:
                ans[1].append(edges[i][3])

        return ans
```

