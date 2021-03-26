# LeetCode题解(1483)：树节点的第K个祖先(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/)（困难）

标签：树、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(NlogN)$ | 844ms (88.24%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class TreeAncestor:
    _POW = 16  # 树的最大深度：50000 < 2^16

    def __init__(self, n: int, parent: List[int]):
        # 初始化状态矩阵
        self.dp = [[-1] * self._POW for _ in range(n)]

        # 构造初始的父节点关系
        for i in range(n):
            self.dp[i][0] = parent[i]

        # 逐层构造动态规划中的祖先关系
        for j in range(1, self._POW):
            for i in range(n):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self._POW - 1, -1, -1):
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break
        return node
```

