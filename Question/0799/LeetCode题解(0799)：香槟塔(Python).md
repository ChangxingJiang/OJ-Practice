# LeetCode题解(0799)：香槟塔(Python)

题目：[原题链接](https://leetcode-cn.com/problems/champagne-tower/)（中等）

标签：动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 144ms (32.52%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def __init__(self):
        self.total_poured = 0

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        self.total_poured = poured

        if query_row == 0 and query_glass == 0:
            return 1 if poured >= 1 else poured

        poured = 0
        if query_glass - 1 >= 0:
            poured += self.overflow(query_row - 1, query_glass - 1) / 2
        if query_glass <= query_row - 1:
            poured += self.overflow(query_row - 1, query_glass) / 2
        return poured if poured <= 1 else 1

    @functools.lru_cache(None)
    def overflow(self, query_row: int, query_glass: int):
        """计算能够溢出的总量"""
        # 最顶层的情况
        if query_row == 0 and query_glass == 0:
            return self.total_poured - 1 if self.total_poured > 1 else 0

        # 非最顶层的情况
        poured = 0
        if query_glass - 1 >= 0:
            poured += self.overflow(query_row - 1, query_glass - 1) / 2
        if query_glass <= query_row - 1:
            poured += self.overflow(query_row - 1, query_glass) / 2
        return poured - 1 if poured > 1 else 0
```

