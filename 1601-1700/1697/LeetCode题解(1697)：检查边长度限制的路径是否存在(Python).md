# LeetCode题解(1697)：检查边长度限制的路径是否存在(Python)

题目：[原题链接](https://leetcode-cn.com/problems/checking-existence-of-edge-length-limited-paths/)（困难）

标签：排序、并查集

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 680ms (60%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n)

        lst = {tuple(elem): i for i, elem in enumerate(queries)}

        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])

        ans = [False] * len(queries)

        i = 0
        for query in queries:
            while i < len(edgeList) and edgeList[i][2] < query[2]:
                dsu.union(edgeList[i][0], edgeList[i][1])
                i += 1
            ans[lst[tuple(query)]] = (dsu.find(query[0]) == dsu.find(query[1]))

        return ans
```

