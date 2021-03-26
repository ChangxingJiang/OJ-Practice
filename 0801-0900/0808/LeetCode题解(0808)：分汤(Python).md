# LeetCode题解(0808)：分汤(Python)

题目：[原题链接](https://leetcode-cn.com/problems/soup-servings/)（中等）

标签：动态规划、记忆化递归

| 解法           | 时间复杂度             | 空间复杂度             | 执行用时      |
| -------------- | ---------------------- | ---------------------- | ------------- |
| Ans 1 (Python) | $O(min(N,200^2))=O(1)$ | $O(min(N,200^2))$=O(1) | 36ms (98.92%) |
| Ans 2 (Python) |                        |                        |               |
| Ans 3 (Python) |                        |                        |               |

解法一：

```python
class Solution:
    def soupServings(self, N: int) -> float:
        @functools.lru_cache(None)
        def dfs(n, m):
            if n <= 0 and m <= 0:
                return 0.5
            elif n <= 0:
                return 1
            elif m <= 0:
                return 0
            else:
                return 0.25 * (dfs(n - 100, m - 0) + dfs(n - 75, m - 25) + dfs(n - 50, m - 50) + dfs(n - 25, m - 75))

        if N >= 5000:
            return 1  # 近似处理
        else:
            return dfs(N, N)
```

