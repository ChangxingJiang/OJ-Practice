# LeetCode题解(1774)：最接近目标价格的甜点成本(Python)

题目：[原题链接](https://leetcode-cn.com/problems/closest-dessert-cost/)（中等）

标签：动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×2^M)$ | $O(N+M)$   | 76ms (77.53%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = 10 ** 9

    def closestCost(self, base_costs: List[int], topping_costs: List[int], target: int) -> int:
        size = len(topping_costs)
        topping_costs.sort()

        @functools.lru_cache(None)
        def dfs(i, now):
            """深度优先搜索:i=当前配料位置，now=当前总成本"""
            if i == size or now > target:
                if (abs(now - target) < abs(self.ans - target) or
                        (abs(now - target) == abs(self.ans - target) and now < self.ans)):
                    self.ans = now
                return

            for k in [0, 1, 2]:
                dfs(i + 1, now + k * topping_costs[i])

        for v in base_costs:
            dfs(0, v)

        return self.ans
```

