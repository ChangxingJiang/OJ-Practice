# LeetCode题解(0279)：完全平方数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/perfect-squares/)（中等）

标签：数学、深度优先搜索、动态规划

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时      |
| -------------- | ------------- | ---------- | ------------- |
| Ans 1 (Python) | --            | --         | 超出时间限制  |
| Ans 2 (Python) | $O(\sqrt{N})$ | $O(1)$     | 40ms (99.00%) |
| Ans 3 (Python) |               |            |               |

解法一（暴力解法）：

```python
class Solution:
    def __init__(self):
        self.squares = []

    def numSquares(self, n: int) -> int:
        self.squares = [i ** 2 for i in range(1, int(pow(n, 0.5)) + 1)]
        return self.dfs(n, len(self.squares) - 1)

    @functools.lru_cache(None)
    def dfs(self, n, idx):
        # 处理递归完成的情况
        if n == 0:
            return 0
        if idx == 0:
            return n

        # 处理递归未完成的情况
        res = self.dfs(n, idx - 1)
        for i in range(1, n // self.squares[idx] + 1):
            res = min(res, self.dfs(n - i * self.squares[idx], idx - 1) + i)

        return res
```

解法二：

```python
class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(v):
            t = int(pow(v, 0.5))
            return t * t == v

        while n % 4 == 0:
            n //= 4

        # 三平方定理
        if n % 8 == 7:
            return 4

        # 直接为完全平方数
        if is_square(n):
            return 1

        # 判断是否如果可以由两个平方数组成
        for i in range(1, int(pow(n, 0.5)) + 1):
            if is_square(n - i * i):
                return 2

        return 3
```

