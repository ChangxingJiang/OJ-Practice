# LeetCode题解(0947)：移除最多的同行或同列石头(Python)

题目：[原题链接](https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/)（中等）

标签：并查集、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (96.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class DSU:
    def __init__(self, n: int):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i: int):
        """查询i所属的连通分支"""
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i: int, j: int):
        """合并i和j的连通分支"""
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]

    def group_num(self):
        """计算当前的连通分支数量"""
        groups = set()
        for i in range(len(self.array)):
            if self.array[i] not in groups and self.find(i) not in groups:
                groups.add(self.find(i))
        return len(groups)

    def __repr__(self):
        return str(len(self.array)) + ":" + str(self.array)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)

        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)

        dsu = DSU(len(stones))

        for lst in rows.values():
            for j in range(len(lst) - 1):
                dsu.union(lst[j], lst[j + 1])
        for lst in cols.values():
            for j in range(len(lst) - 1):
                dsu.union(lst[j], lst[j + 1])

        return len(stones) - dsu.group_num()
```

