# LeetCode题解(1627)：带阈值的图连通性(Python)

题目：[原题链接](https://leetcode-cn.com/problems/graph-connectivity-with-threshold/)（困难）

标签：图、数学、并查集

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 200ms (75%) |
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


# 计算最大公因数
def count_hcf(t, x, y):
    if t == 0:
        return True
    for i in range(t + 1, min(x, y) + 1):
        if (x % i == 0) and (y % i == 0):
            return True


# 计算最大公因数
def count_hcf_2(t, x, y):
    while x % y != 0:
        x, y = y, (x % y)
        if y <= t:
            return False
    return y > t


class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # 处理特殊情况
        if threshold == 0:
            return [True] * len(queries)

        # 定义并查集
        dsu = DSU(n + 1)

        # 计算通路
        for i in range(threshold + 1, n):
            j = 1
            while i * (j + 1) <= n:
                dsu.union(i * j, i * (j + 1))
                j += 1

        # 计算结果
        ans = []
        for query in queries:
            ans.append(dsu.find(query[0]) == dsu.find(query[1]))
        return ans
```